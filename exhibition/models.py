# -*- coding: utf-8 -*-
import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Collector(models.Model):
	name = models.CharField(u'Имя', max_length=55)
	surname = models.CharField(u'Фамилия', max_length=55)
	date_of_birth = models.DateField(u'День Рождения')
	email = models.EmailField('Email')
	phone = models.CharField(u'Телефон', max_length=15)
	address = models.CharField(u'Адрес', max_length=55, null=True, blank=True)
	skype = models.CharField('Skype', max_length=55, null=True, blank=True)

	def __unicode__(self):
		return self.name + ' ' + self.surname
	
class Collection(models.Model):
	name = models.CharField(u'Название коллекции', max_length=55)
	description = models.TextField(u'Описание', null=True, blank=True)
	collector = models.ForeignKey(Collector, verbose_name=u'Коллекционер')

	def __unicode__(self):
		return self.name

class Exhibition(models.Model):
	name = models.CharField(u'Назвние выставки', max_length=55)
	date = models.DateTimeField(u'Дата и время проведения')
	short_description = models.CharField(u'Краткое описание', max_length=255)
	description = models.TextField(u'Описание', null=True, blank=True)
	collection = models.ManyToManyField(Collection, verbose_name=u'Коллекции')

	def __unicode__(self):
		return self.name

