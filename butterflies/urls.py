from django.conf.urls import patterns, include, url, handler404
from django.contrib import admin
from butterflies.views import contact, custom_page_not_found
from exhibition.views import list_of_exhibition
from django.http import HttpResponse
from django.shortcuts import render


urlpatterns = patterns('',
    url(r'^$', list_of_exhibition, name='index'),
    url(r'^contact/$', contact, name='contact'),
    url(r'^collector/', include('collector.urls', namespace="collector")),
    url(r'^sponsor/', include('sponsors.urls', namespace="sponsor")),
    url(r'^exhibition/', include('exhibition.urls', namespace="exhibition")),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^quadratic/', include('quadratic.urls', namespace="quadratic")),
    url(r'^admin/', include(admin.site.urls)),
	url(r'$', custom_page_not_found, name='404'),
)


