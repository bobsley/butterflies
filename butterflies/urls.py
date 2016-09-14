from django.conf.urls import patterns, include, url
from django.contrib import admin
from butterflies import views
from django.http import HttpResponse
from django.shortcuts import render


urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.index, name='index'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^butterfly_list/$', views.butterfly_list, name='butterfly_list'),
    url(r'^morpho_rhetenor/$', views.morpho_rhetenor, name='morpho_rhetenor'),
    # url(r'^$', 'butterflies.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^quadratic/', include('quadratic.urls', namespace="quadratic")),
    url(r'^admin/', include(admin.site.urls)),
)
