from django.conf.urls import patterns, url
from sponsors.views import list_of_sponsor, detail

urlpatterns = patterns('',
	#url(r'^$', list_of_sponsor, name='list'),
    url(r'^(?P<num>\w+)/$', detail, name='detail'),
	)