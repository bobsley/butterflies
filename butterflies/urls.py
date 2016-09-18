from django.conf.urls import patterns, include, url
from django.contrib import admin
from butterflies.views import contact
from exhibition.views import list_of_exhibition, exhibition_details, list_of_collector, collector_details
from django.http import HttpResponse
from django.shortcuts import render


urlpatterns = patterns('',
    url(r'^$', list_of_exhibition, name='index'),
    url(r'^contact/$', contact, name='contact'),
    url(r'^collector_list/$', list_of_collector, name='list_of_collector'),
    url(r'^collector/(?P<num>\w*)$', collector_details, name='collector_details'),
    url(r'^exhibition/(?P<num>\w*)$', exhibition_details, name='exhibition_details'),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^quadratic/', include('quadratic.urls', namespace="quadratic")),
    url(r'^admin/', include(admin.site.urls)),
)
