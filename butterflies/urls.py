from django.conf.urls import patterns, include, url
from django.contrib import admin
from butterflies import views
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	return render(request, 'index.html')

def contact(request):
	return render(request, 'contact.html')

def butterfly_list(request):
	return render(request, 'butterfly_list.html')

def morpho_rhetenor(request):
	return render(request, 'morpho_rhetenor.html')

urlpatterns = patterns('',
    # Examples:
    url(r'^$', index, name='index'),
    url(r'^contact/$', contact, name='contact'),
    url(r'^butterfly_list/$', butterfly_list, name='butterfly_list'),
    url(r'^morpho_rhetenor/$', morpho_rhetenor, name='morpho_rhetenor'),
    # url(r'^$', 'butterflies.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
)
