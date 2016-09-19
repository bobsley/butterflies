from django.conf.urls import patterns, url
from collector.views import list_of_collector, detail

urlpatterns = patterns('',
	url(r'^$', list_of_collector, name='list'),
    url(r'^(?P<num>\w+)/$', detail, name='detail'),
	)