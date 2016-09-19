# -*- coding: utf-8 -*-
from django.contrib import admin
from sponsors.models import Sponsor

# Register your models here.

class SponsorAdmin(admin.ModelAdmin):
	fieldsets = [
		(u'Основная информация',   {'fields': ['user', 'date_of_birth', 'gender']}),
		(u'Контактная информация', {'fields': ['phone', 'address', 'skype']}),
		(u'Описание',              {'fields': ['description']}),
	]
	list_display = ('user_full_name', 'gender', 'skype', 'description')
	#list_filter = ['user_is_staff']

admin.site.register(Sponsor, SponsorAdmin)
