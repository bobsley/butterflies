from django.conf.urls import patterns, url
from exhibition.views import ExhibitionDetailView, ExhibitionCreateView, ExhibitionUpdateView, ExhibitionDeleteView

urlpatterns = patterns('',
    url(r'^detail/(?P<pk>\w+)/$', ExhibitionDetailView.as_view(), name='detail'),
    url(r'^add/$', ExhibitionCreateView.as_view(), name='create'),
	url(r'^edit/(?P<pk>\w+)/$', ExhibitionUpdateView.as_view(), name='edit'),
	url(r'^delete/(?P<pk>\w+)/$', ExhibitionDeleteView.as_view(), name='delete'),
    )