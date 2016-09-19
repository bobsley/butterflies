from django.conf.urls import patterns, url
from exhibition.views import detail

urlpatterns = patterns('',
    url(r'^(?P<num>\w+)/$', detail, name='detail'),
    )