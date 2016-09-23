from django.conf.urls import patterns, url
from exhibition.views import detail, create, edit, remove

urlpatterns = patterns('',
    url(r'^detail/(?P<pk>\w+)/$', detail, name='detail'),
    url(r'^add/$', create, name='create'),
	url(r'^edit/(?P<pk>\w+)/$', edit, name='edit'),
	url(r'^remove/(?P<pk>\w+)/$', remove, name='remove'),
    )