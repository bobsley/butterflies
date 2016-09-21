# -*- coding: utf-8 -*-
from datetime import datetime
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from exhibition.models import Exhibition, Collection
from sponsors.models import Sponsor

# Create your views here.
def list_of_exhibition(request):
	exhibitions = []
	exhibitions1 = Exhibition.objects.all()#filter(date=datetime.now())
	for exhibition in exhibitions1:
		if exhibition.date.year > datetime.now().year:
			exhibitions.append(exhibition)
		if exhibition.date.month > datetime.now().month and exhibition.date.year == datetime.now().year:
			exhibitions.append(exhibition)
		if exhibition.date.day > datetime.now().day and exhibition.date.month == datetime.now().month and exhibition.date.year == datetime.now().year:
			exhibitions.append(exhibition)
		if exhibition.date.hour > datetime.now().hour and exhibition.date.day == datetime.now().day and exhibition.date.month == datetime.now().month and exhibition.date.year == datetime.now().year:
			exhibitions.append(exhibition)
		if exhibition.date.minute > datetime.now().minute and exhibition.date.hour == datetime.now().hour and exhibition.date.day == datetime.now().day and exhibition.date.month == datetime.now().month and exhibition.date.year == datetime.now().year:
			exhibitions.append(exhibition)
		if exhibition.date.second > datetime.now().second and exhibition.date.minute == datetime.now().minute and exhibition.date.hour == datetime.now().hour and exhibition.date.day == datetime.now().day and exhibition.date.month == datetime.now().month and exhibition.date.year == datetime.now().year:
			exhibitions.append(exhibition)
	return render(request, 'index.html', {'exhibitions': exhibitions})


def detail(request, num):
	exhibition = Exhibition.objects.get(id=num)
	#collection = Collection.objects.values('name').get(exhibition__id=num)
	collections = Collection.objects.filter(exhibition__pk=num)
	sponsors = Sponsor.objects.filter(sponsor_exhibition__pk=num)
	assistants = Sponsor.objects.filter(assistant_exhibition__pk=num)
	
	return render(request, 'exhibition/detail.html', {'exhibition': exhibition, 'collections': collections, 'sponsors': sponsors, 'assistants': assistants})

