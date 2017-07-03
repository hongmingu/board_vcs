from django.shortcuts import render
from post.models import PostAll
from datetime import datetime, timedelta
from django.http import HttpResponse, JsonResponse

# Create your views here.
def postAllList(request):
    if request.method == "GET":
        if request.is_ajax():
            querysetlist = PostAll.objects.all()
            context = {'do': querysetlist}
            lastId = request.GET.get('last', 0)
            # elasped_minutes = datetime.now() - timedelta(seconds=10)
            # list_i = PostAll.objects.filter(created_date__gte=elasped_minutes).order_by("CreatedAt")
            matched_list = PostAll.objects.all().filter(id__gt = lastId)
            hello = list(matched_list.values('createdAt','id','text'))
            return JsonResponse(hello, safe=False)
        else:
            querysetlist = PostAll.objects.all()
            context = {'do': querysetlist}
            # elasped_minutes = datetime.now() - timedelta(seconds=10)
            # list_i = PostAll.objects.filter(created_date__gte=elasped_minutes).order_by("CreatedAt")
            return render (request, 'base.html', context)
    return 0