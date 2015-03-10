from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext, loader
import random

from imager_images.models import Photo


def home(request):
    photos = Photo.objects.all()
    random_image = random.choice(photos)

    context = {'random_image': random_image.picture, 'request': request}
    return render(request, 'home.html', {'context': context})


def login(request):
    pass


def logout(request):
    pass


def register(request):
    pass


def activate(request):
    pass

