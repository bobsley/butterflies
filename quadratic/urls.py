from django.conf.urls import patterns, url

from quadratic import views

urlpatterns = patterns('',
    url(r'^results/a=(?P<a>(-|)\w*)&b=(?P<b>(-|)\w*)&c=(?P<c>(-|)\w*)/$', views.quadratic_results, name='quadratic_results'),
)