# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

# Create your views here.
def quadratic_results(request, a, b, c):
	#form = QuadraticForm()
	#a = request.GET.get('a')
	#b = request.GET.get('b')
	#c = request.GET.get('c')#.split('/')[0]
	a = a
	b = b
	c = c
	
	error_message_a = ''
	error_message_b = ''
	error_message_c = ''
	message_discr = ''
	message = ''
	roots = ''
	error = False
	if not a:
		error_message_a = u'коэффициент не определен'
		error = True
	elif not a.isdigit() and '-' not in a:
		error_message_a = u'коэффициент не целое число'
		error = True
	elif int(a) == 0:
		error_message_a = u'коэффициент при первом слагаемом уравнения не может быть равным нулю'
		error = True
			
	if not b:
		error_message_b = u'коэффициент не определен'
		error = True
	elif not b.isdigit() and '-' not in b:
		error_message_b = u'коэффициент не целое число'
		error = True
	if not c:
		error_message_c = u'коэффициент не определен'
		error = True
	elif not c.isdigit() and '-' not in c:
		error_message_c = u'коэффициент не целое число'
		error = True
	if not error:
		if '-' in a:
			a = -int(a[1:])
		else:
			a = int(a)
		if '-' in b:
			b = -int(b[1:])
		else:
			b = int(b)
		if '-' in c:
			c = -int(c[1:])
		else:
			c = int(c)
		discr = pow(b, 2.0) - 4 * a * c
		message_discr = u'Дискриминант: {}'.format(discr)
		if discr < 0:
			message = u'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
			roots = ''
		elif discr == 0:
			x1 = round(float(-b / (2.0*a)),1)
			message = u'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень:'
			roots = 'x = {}'.format(x1)
		elif discr > 0:
			x1 = round(float((-b + (b*b - 4*a*c)**(1/2.0)) / (2.0*a)), 1)
			x2 = round(float((-b - (b*b - 4*a*c)**(1/2.0)) / (2.0*a)), 1)
			message = u'Квадратное уравнение имеет два действительных корня:'
			roots = 'x1 = {}, x2 = {}'.format(x1, x2)
	return render(request, 'results.html', {'a':a, 'b':b, 'c':c, 'error_message_a':error_message_a, 'error_message_b':error_message_b, 'error_message_c':error_message_c, 'message_discr':message_discr, 'message':message, 'roots':roots})