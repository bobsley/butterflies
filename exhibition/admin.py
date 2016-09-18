# -*- coding: utf-8 -*-
from django.contrib import admin
from exhibition.models import Collector, Collection, Exhibition

# Register your models here.


class CollectorAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,        {'fields': ['name', 'surname', 'date_of_birth']}),
		(u'Контактная информация', {'fields': ['email', 'phone', 'address', 'skype']}),
	]
	list_display = ('surname', 'name', 'phone')
	list_filter = ['surname']
	search_fields = ['name', 'surname']

class CollectionAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,               {'fields': ['name', 'collector']}),
		(u'Описание', {'fields': ['description'], 'classes': ['collapse']}),
	]
	list_filter = ['name']
	search_fields = ['name', 'collector']

class ExhibitionAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,               {'fields': ['name', 'date', 'short_description', 'collection']}),
		(u'Описание', {'fields': ['description'], 'classes': ['collapse']}),
	]
	list_display = ('name', 'date')
	list_filter = ['date']
	search_fields = ['name', 'date']

admin.site.register(Collector, CollectorAdmin)
admin.site.register(Collection, CollectionAdmin)
admin.site.register(Exhibition, ExhibitionAdmin)