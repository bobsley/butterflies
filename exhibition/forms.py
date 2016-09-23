# -*- coding: utf-8 -*-
from django import forms
from exhibition.models import Exhibition

# Create your views here.
class ExhibitionModelForm(forms.ModelForm):
	class Meta:
		model = Exhibition