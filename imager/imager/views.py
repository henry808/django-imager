from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext, loader

def home(request, *args, **kwargs):
    context = {'name': 'bob'}
    return render(request, 'home.html', context)
