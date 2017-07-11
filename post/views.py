from django.shortcuts import render
from post.models import *
from datetime import datetime, timedelta
from django.http import HttpResponse, JsonResponse

# Create your views here.
def postList(request):
    if request.method == "GET":
        elasped_seconds = datetime.now() - timedelta(seconds=60)
        type = request.GET.get('t', 0)
        lastId = request.GET.get('l', 0)
        dodo = PostAll
        if request.is_ajax():
            if type == 'submitBtn':
                content = request.GET.get('c', 'Wrong Sentences or Wrong Process Happend')
                postToSave = PostAll(text = content)
                postToSave.save()
                list_i = PostAll.objects.filter(createdAt__gte=elasped_seconds).filter(id__gt = lastId).order_by("createdAt")
                toGoList = list(list_i.values('id', 'text', 'createdAt'))
                return JsonResponse(toGoList, safe=False)
            elif type =='refreshBtn' :
                list_i = PostAll.objects.filter(createdAt__gte=elasped_seconds).filter(id__gt = lastId).order_by("createdAt")
                toGoList = list(list_i.values('id', 'text', 'createdAt'))
                return JsonResponse(toGoList, safe=False)
            else:
                return JsonResponse({'res':"You've got wrong response or no AjaxResponse"}, safe=False)
        else:
            list_i = dodo.objects.filter(createdAt__gte=elasped_seconds).filter(id__gt=lastId).order_by("-createdAt")
            toGoList = {
                'posts' : list_i,
            }
            return render(request, 'base.html', toGoList)

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
    if request.method == "GET":
        elasped_seconds = datetime.now() - timedelta(seconds=60)
        type = request.GET.get('t', 0)
        lastId = request.GET.get('l', 0)
        earlyId = request.GET.get('e',0)

        postByLang = switch(language)
        temByLang = switchTem(language)


        if request.is_ajax():
            if type == 'submitBtn':
                content = request.GET.get('c', 'Wrong Sentences or Wrong Process Happend')
                postToSave = postByLang(text = content)
                postToSave.save()
                querysetList = postByLang.objects.filter(createdAt__gte=elasped_seconds).filter(id__gt = lastId).order_by("-createdAt")
                toGoList = list(querysetList.values('id', 'text', 'createdAt'))
                return JsonResponse(toGoList, safe=False)
            elif type =='refreshBtn' :
                querysetList = postByLang.objects.filter(createdAt__gte=elasped_seconds).filter(id__gt = lastId).order_by("-createdAt")
                toGoList = list(querysetList.values('id', 'text', 'createdAt'))
                return JsonResponse(toGoList, safe=False)
            elif type == 'moreLoad':
                querysetList = postByLang.objects.filter(createdAt__gte=elasped_seconds).filter(id__lt=earlyId).order_by(
                    "-createdAt")[:2]
                toGoList = list(querysetList.values('id', 'text', 'createdAt'))
                return JsonResponse(toGoList, safe=False)
            else:
                return JsonResponse({'res':"You've got wrong response or no AjaxResponse"}, safe=False)
        else:
            querysetList = postByLang.objects.filter(createdAt__gte=elasped_seconds).filter(id__gt=lastId).order_by("-createdAt")[:2]
            toGoList = {
                'posts' : querysetList,
            }
            return render(request, temByLang, toGoList)

def postMonthList(request):
    if request.method == 'GET':
        elasped_days = datetime.now() - timedelta(days=30)
        type =request.GET.get('t',0)
        lastId = request.GET.get('l',0)
        earlyId = request.GET.get('e',0)

        if request.is_ajax():
            if type == 'submitBtn':
                content = request.GET.get('c', 'Wrong Sentences or Wrong Process Happend')
                postToSave = PostForMonth(text=content)
                postToSave.save()
                querysetList = PostForMonth.objects.filter(createdAt__gte=elasped_days).filter(id__gt = lastId).order_by("-createdAt")
                toGoList = list(querysetList.values('id', 'text', 'createdAt'))
                return JsonResponse(toGoList, safe=False)
            elif type == 'refreshBtn':
                querysetList = PostForMonth.objects.filter(createdAt__gte=elasped_days).filter(id__gt=lastId).order_by(
                "-createdAt")
                toGoList = list(querysetList.values('id', 'text', 'createdAt'))
                return JsonResponse(toGoList, safe=False)
            elif type == 'moreLoad':
                querysetList = PostForMonth.objects.filter(createdAt__gte=elasped_days).filter(id__lt=earlyId).order_by(
                    "-createdAt")[:5]
                toGoList = list(querysetList.values('id', 'text', 'createdAt'))
                return JsonResponse(toGoList, safe=False)
            else:
                return JsonResponse({'res': "You've got wrong response or no AjaxResponse"}, safe=False)
        else:
            querysetList = PostForMonth.objects.filter(createdAt__gte=elasped_days).filter(id__gt=lastId).order_by(
                "-createdAt")[:5]
            toGoList = {
                'posts': querysetList,
            }
            return render(request, 'forMonth.html', toGoList)