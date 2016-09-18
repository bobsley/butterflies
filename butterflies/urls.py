from django.conf.urls import patterns, include, url
from django.contrib import admin
from butterflies.views import index, contact, butterfly_list, morpho_rhetenor
from exhibition.views import list_of_exhibition, exhibition_details
from django.http import HttpResponse
from django.shortcuts import render


urlpatterns = patterns('',
    url(r'^$', list_of_exhibition, name='index'),
    url(r'^contact/$', contact, name='contact'),
    url(r'^butterfly_list/$', butterfly_list, name='butterfly_list'),
    url(r'^morpho_rhetenor/$', morpho_rhetenor, name='morpho_rhetenor'),
    url(r'^exhibition/(?P<num>\w*)$', exhibition_details, name='exhibition_details'),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^quadratic/', include('quadratic.urls', namespace="quadratic")),
    url(r'^admin/', include(admin.site.urls)),
)
