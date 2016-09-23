from django.conf.urls import patterns, url
from collector.views import list_of_collector, detail, create, edit, remove

urlpatterns = patterns('',
	url(r'^$', list_of_collector, name='list'),
	url(r'^add/$', create, name='create'),
	url(r'^edit/(?P<pk>\w+)/$', edit, name='edit'),
	url(r'^remove/(?P<pk>\w+)/$', remove, name='remove'),
    url(r'^detail/(?P<pk>\w+)/$', detail, name='detail'),
	)