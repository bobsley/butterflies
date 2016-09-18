# -*- coding: utf-8 -*-
from datetime import datetime
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from exhibition.models import Collector, Collection, Exhibition

# Create your views here.
def list_of_exhibition(request):
	exhibitions = Exhibition.objects.all()
	exhibit = []
	for exhibition in exhibitions:
		if exhibition.date.year > datetime.now().year:
			exhibit.append(exhibition)
		if exhibition.date.month > datetime.now().month and exhibition.date.year == datetime.now().year:
			exhibit.append(exhibition)
		if exhibition.date.day >= datetime.now().day and exhibition.date.month == datetime.now().month and exhibition.date.year == datetime.now().year:
			exhibit.append(exhibition)
	return render(request, 'index.html', {'exhibitions': exhibit})

def exhibition_details(request, num):
	num=num
	exhibition = Exhibition.objects.get(id=num)
	return render(request, 'exhibition_details.html', {'exhibition': exhibition})

def list_of_collector(request):
	collectors = Collector.objects.all()
	return render(request, 'collector_list.html', {'collectors': collectors})

def collector_details(request, num):
	num=num
	collector = Collector.objects.get(id=num)
	return render(request, 'collector_details.html', {'collector': collector})