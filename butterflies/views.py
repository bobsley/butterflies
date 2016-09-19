from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic


def contact(request):
	return render(request, 'contact.html')

def morpho_rhetenor(request):
	return render(request, 'morpho_rhetenor.html')