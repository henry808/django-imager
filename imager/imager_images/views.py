from django.shortcuts import render
from django.views.generic import ListView
from imager_images.models import Photo
#from imager_users.forms import ImagerProfileEditForm # to override form

class StreamView(ListView):
    model = Photo
    template_name = "stream.html"


def library_view(request, *args, **kwargs):
    print kwargs
    return render(request, 'library.html', {})
