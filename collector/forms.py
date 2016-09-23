# -*- coding: utf-8 -*-
from django import forms
from collector.models import Collector
from exhibition.models import Collection

# Create your views here.
class CollectorModelForm(forms.ModelForm):
	class Meta:
		model = Collector

class CollectionModelForm(forms.ModelForm):
	class Meta:
		model = Collection