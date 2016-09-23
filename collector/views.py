# -*- coding: utf-8 -*-
from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from collector.models import Collector
from exhibition.models import Collection
from collector.forms import CollectorModelForm, CollectionModelForm
from django.contrib import messages

# Create your views here.
def list_of_collector(request):
	collectors = Collector.objects.all()
	return render(request, 'collector/list.html', {'collectors': collectors})

def detail(request, pk):
	collector = Collector.objects.get(id=pk)
	collections = Collection.objects.filter(collector__pk=pk)
	return render(request, 'collector/detail.html', {'collector': collector, 'collections':collections})

def create(request):
	if request.method =='POST':
		form = CollectorModelForm(request.POST)
		if form.is_valid():
			application = form.save()
			mes = u'Коллекционер {} {} успешно добавлен.'.format(application.surname, application.name)
			messages.success(request, mes)
			return redirect('collector:list')
	else:
		form = CollectorModelForm()
		return render(request, 'collector/add.html', {'form':form})

def edit(request, pk):
	application = Collector.objects.get(id=pk)
	if request.method =='POST':
		form = CollectorModelForm(request.POST, instance=application)
		if form.is_valid():
			application = form.save()
			mes = u'Данные изменены.'
			messages.success(request, mes)
	else:
		form = CollectorModelForm(instance=application)
	return render(request, 'collector/edit.html', {'form':form})

def remove(request, pk):
	application = Collector.objects.get(id=pk)
	if request.method =='POST':
			application.delete()
			mes = u'Коллекционер {} {} был удален.'.format(application.surname, application.name)
			messages.success(request, mes)
			return redirect('collector:list')
	return render(request, 'collector/remove.html', {'collector':application})

def add_collection(request, pk):
	collector = Collector.objects.get(id=pk)
	if request.method =='POST':
		form = CollectionModelForm(request.POST)
		if form.is_valid():
			application = form.save()
			mes = u'Коллекция {} успешно добавлена.'.format(application.name)
			messages.success(request, mes)
			return redirect('collector:list')
	else:
		form = CollectionModelForm(initial={'collector': collector})
		return render(request, 'collector/add_collection.html', {'form':form, 'collector': collector})