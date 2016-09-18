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
	#for exhibition in exhibitions:
	#	if exhibition.date.year <= datetime.now().year:
	#		if exhibition.date.month <= datetime.now().month:
	#			if exhibition.date.day < datetime.now().day:
	#				exhibitions.delete()
	return render(request, 'index.html', {'exhibitions': exhibitions})

def exhibition_details(request, num):
	num=num
	exhibition = Exhibition.objects.get(id=num)
	return render(request, 'exhibition_details.html', {'exhibition': exhibition})