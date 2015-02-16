from django.shortcuts import render

from django.http import HttpResponse

def persona_view(request):
	return HttpResponse('Ok')
