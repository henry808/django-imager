from django.shortcuts import render
# from django.http import HttpResponse, HttpResponseRedirect, Http404
# from django.template import RequestContext, loader
from settings import MEDIA_URL, STATIC_URL
import random

from imager_images.models import Photo


def home(request):
    photos = Photo.objects.filter(published=Photo.PUBLIC)

    if photos.count():
        location = MEDIA_URL
        random_image = random.choice(photos).picture
    else:
        location = STATIC_URL
        random_image = './images/default_profile_image.jpg'
    context = {'random_image': random_image,
               'request': request,
               'image_location': location}
    return render(request, 'home.html', {'context': context})