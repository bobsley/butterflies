# -*- coding: utf-8 -*-
from datetime import datetime
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from collector.models import Collector

# Create your views here.
def list_of_collector(request):
	collectors = Collector.objects.all()
	return render(request, 'collector/list.html', {'collectors': collectors})

def detail(request, num):
	num=num
	collector = Collector.objects.get(id=num)
	return render(request, 'collector/detail.html', {'collector': collector})