from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext, loader


def home(request):
    context = {'random_image': 'something else', 'request': request}
    return render(request, 'home.html', {'context': context})


def login(request):
    pass


def logout(request):
    pass


def register(request):
    pass


def activate(request):
    pass
