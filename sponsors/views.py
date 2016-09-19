# -*- coding: utf-8 -*-
from datetime import datetime
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from sponsors.models import Sponsor

# Create your views here.
def list_of_sponsor(request):
	sponsors = Sponsor.objects.all()
	return render(request, 'sponsors/list.html', {'sponsors': sponsors})

def detail(request, num):
	num=num
	sponsor = Sponsor.objects.get(id=num)
	return render(request, 'sponsors/detail.html', {'sponsor': sponsor})