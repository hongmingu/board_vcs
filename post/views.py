from django.shortcuts import render, render_to_response
from django.template import RequestContext
from post.models import *
from datetime import datetime, timedelta
from django.utils import timezone
from django.http import JsonResponse

# Create your views here.

def switch(x):
    return {
        'all': PostAll,
        'ara': PostArabic,
        'ben': PostBengali,
        'chi': PostChinese,
        'eng': PostEnglish,
        'fre': PostFrench,
        'ger': PostGerman,
        'hin': PostHindi,
        'jap': PostJapanese,
        'jav': PostJavanese,
        'kor': PostKorean,
        'lah': PostLahnda,
        'mal': PostMalay,
        'por': PostPortuguese,
        'rus': PostRussian,
        'spa': PostSpanish,
        'tel': PostTelugu,
    }.get(x, PostAll)

def switchTem(x):
    return {
        'all': 'all.html',
        'ara': 'ara.html',
        'ben': 'ben.html',
        'chi': 'chi.html',
        'eng': 'eng.html',
        'fre': 'fre.html',
        'ger': 'ger.html',
        'hin': 'hin.html',
        'jap': 'jap.html',
        'jav': 'jav.html',
        'kor': 'kor.html',
        'lah': 'lah.html',
        'mal': 'mal.html',
        'por': 'por.html',
        'rus': 'rus.html',
        'spa': 'spa.html',
        'tel': 'tel.html',
    }.get(x, 'all.html')

def postLanguageList(request, language):
    pbyl = switch(language)
    tbyl = switchTem(language)
    es = timezone.now() - timedelta(seconds=60)

    if request.method == "POST":
        t = request.POST.get('t', 0)
        l = request.POST.get('l', 0)
        if request.is_ajax():
            if t == 'submitBtn':
                c = request.POST.get('c', 'Wrong Sentences or Wrong Process Happend')
                pts = pbyl(text = c)
                pts.save()
                ql = pbyl.objects.filter(createdAt__gte=es).filter(id__gt = l).order_by("-createdAt")
                tgl = list(ql.values('id', 'text', 'createdAt'))
                return JsonResponse(tgl, safe=False)
            else:
                return JsonResponse({'res':"You've got wrong response or no AjaxResponse"}, safe=False)

    elif request.method == 'GET':
        t = request.GET.get('t', 0)
        l = request.GET.get('l', 0)
        e = request.GET.get('e',0)

        if request.is_ajax():
            if t =='refreshBtn' :
                ql = pbyl.objects.filter(createdAt__gte=es).filter(id__gt = l).order_by("-createdAt")
                tgl = list(ql.values('id', 'text', 'createdAt'))
                return JsonResponse(tgl, safe=False)
            elif t == 'moreLoad':
                ql = pbyl.objects.filter(createdAt__gte=es).filter(id__lt=e).order_by("-createdAt")[:5]
                tgl = list(ql.values('id', 'text', 'createdAt'))
                return JsonResponse(tgl, safe=False)
            else:
                return JsonResponse({'res': "You've got wrong response or no AjaxResponse"}, safe=False)

        else:
            ql = pbyl.objects.filter(createdAt__gte=es).order_by("-createdAt")[:15]
        tgl = {
            'posts' : ql,
        }
        return render(request, tbyl, tgl)

    else:
        return JsonResponse({'res': "You've used wrong request"}, safe=False)


def postMonthList(request):
    ed = timezone.now() - timedelta(days=30)

    if request.method == 'POST':
        t =request.POST.get('t',0)
        l = request.POST.get('l',0)

        if request.is_ajax():
            if t == 'submitBtn':
                c = request.POST.get('c', 'Wrong Sentences or Wrong Process Happend')
                sc = c[:24]
                pts = PostForMonth(title=sc, text=c)
                pts.save()
                ql = PostForMonth.objects.filter(createdAt__gte=ed).filter(id__gt = l).order_by("-createdAt")
                tgl = list(ql.values('id', 'title', 'createdAt'))
                return JsonResponse(tgl, safe=False)

            else:
                return JsonResponse({'res': "You've got wrong response or no AjaxResponse"}, safe=False)
    elif request.method=='GET':

        if request.is_ajax():
            t = request.GET.get('t', 0)
            l = request.GET.get('l', 0)
            e = request.GET.get('e', 0)
            if t == 'refreshBtn':
                ql = PostForMonth.objects.filter(createdAt__gte=ed).filter(id__gt=l).order_by("-createdAt")
                tgl = list(ql.values('id', 'title', 'createdAt'))
                return JsonResponse(tgl, safe=False)
            elif t == 'moreLoad':
                ql = PostForMonth.objects.filter(createdAt__gte=ed).filter(id__lt=e).order_by(
                    "-createdAt")[:5]
                tgl = list(ql.values('id', 'title', 'createdAt'))
                return JsonResponse(tgl, safe=False)
            else:
                return JsonResponse({'res': "You've got wrong response or no AjaxResponse"}, safe=False)

        else:
            ql = PostForMonth.objects.filter(createdAt__gte=ed).order_by("-createdAt")[:15]
            tgl = {
                'posts': ql,
            }
            return render(request, 'forMonth.html', tgl)

    else:
        return JsonResponse({'res': "You've used wrong request"}, safe=False)


def postMonthDetail(request, pk):
    if request.method == 'GET':
        ql = PostForMonth.objects.get(id=pk)
        tgl = {
            'post' : ql
        }
        return render(request, 'forMonthDetail.html', tgl)

def mainStatus(request):
    if request.method == 'GET':
        if request.is_ajax():
            b = []
            elasped_seconds = timezone.now() - timedelta(seconds=60)
            ll = ['all', 'ara', 'ben', 'chi', 'eng', 'fre', 'ger', 'hin', 'jap', 'jav', 'kor', 'lah', 'mal', 'por', 'rus', 'spa', 'tel']
            for lan in ll:
                b.append(switch(lan).objects.filter(createdAt__gte=elasped_seconds).count())

            return JsonResponse(b, safe=False)

def handler404(request):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request):
    response = render_to_response('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response