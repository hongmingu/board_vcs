"""board URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from post import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='main.html'), name='main'),
    url(r'^(?P<language>[a-z]+)/$', views.postLanguageList, name='language'),
    url(r'^hour/list/$', views.postHourList, name='hour'),
    url(r'^hour/list/(?P<pk>[0-9]+)/$', views.postHourDetail, name='hourDetail'),
    url(r'^comment/hour/$', views.commentHour, name='commentHour'),
    url(r'^mainStatus/$', views.mainStatus, name='mainStatus'),
    url(r'^about/1$', TemplateView.as_view(template_name='workingProcess1.html'), name='working1'),
    url(r'^about/2$', TemplateView.as_view(template_name='workingProcess2.html'), name='working2'),
    url(r'^about/3$', TemplateView.as_view(template_name='workingProcess3.html'), name='working3'),
    url(r'^about/4$', TemplateView.as_view(template_name='workingProcess4.html'), name='working4'),
    url(r'^about/5$', TemplateView.as_view(template_name='workingProcess5.html'), name='working5'),
    url(r'^about/6$', TemplateView.as_view(template_name='workingProcess6.html'), name='working6'),

]

'''
    url(r'^comment/month/$', views.commentMonth, name='commentMonth'),
    url(r'^month/list/$', views.postMonthList, name='month'),
    url(r'^month/list/(?P<pk>[0-9]+)/$', views.postMonthDetail, name='monthDetail'),
'''
