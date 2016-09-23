# -*- coding: utf-8 -*-
from django import forms
from collector.models import Collector

# Create your views here.
class CollectorForm(forms.ModelForm):
	class Meta:
		model = Collector