# -*- coding: utf-8 -*-
from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from exhibition.models import Exhibition, Collection
from sponsors.models import Sponsor
from exhibition.forms import ExhibitionModelForm
from django.contrib import messages

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


def detail(request, pk):
	exhibition = Exhibition.objects.get(id=pk)
	collections = Collection.objects.filter(exhibition__pk=pk)
	sponsors = Sponsor.objects.filter(sponsor_exhibition__pk=pk)
	assistants = Sponsor.objects.filter(assistant_exhibition__pk=pk)
	
	return render(request, 'exhibition/detail.html', {'exhibition': exhibition, 'collections': collections, 'sponsors': sponsors, 'assistants': assistants})

def create(request):
	if request.method =='POST':
		form = ExhibitionModelForm(request.POST)
		if form.is_valid():
			application = form.save()
			mes = u'Выставка {} успешно добавлена.'.format(application.name)
			messages.success(request, mes)
			return redirect('index')
	else:
		form = ExhibitionModelForm()
		return render(request, 'exhibition/add.html', {'form':form})

def edit(request, pk):
	application = Exhibition.objects.get(id=pk)
	if request.method =='POST':
		form = ExhibitionModelForm(request.POST, instance=application)
		if form.is_valid():
			application = form.save()
			mes = u'Данные изменены.'
			messages.success(request, mes)
	else:
		form = ExhibitionModelForm(instance=application)
	return render(request, 'exhibition/edit.html', {'form':form})

def remove(request, pk):
	application = Exhibition.objects.get(id=pk)
	if request.method =='POST':
			application.delete()
			mes = u'Высавка {} была удалена.'.format(application.name)
			messages.success(request, mes)
			return redirect('index')
	return render(request, 'exhibition/remove.html', {'collector':application})