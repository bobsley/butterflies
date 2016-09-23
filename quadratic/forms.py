# -*- coding: utf-8 -*-
from django import forms

# Create your views here.
class QuadraticForm(forms.Form):
	a = forms.FloatField(label=u'Коэффициент a', initial=1)
	b = forms.FloatField(label=u'Коэффициент b', initial=0)
	c = forms.FloatField(label=u'Коэффициент c', initial=0)

	def clean_a(self):
		a = self.cleaned_data['a']
		if a == 0:
			raise forms.ValidationError("коэффициент при первом слагаемом уравнения не может быть равным нулю")
		return self.cleaned_data['a']