from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from imager_images.models import Photo, Album
from django.contrib.auth.decorators import login_required
#from imager_users.forms import ImagerProfileEditForm # to override form


class StreamView(ListView):
    model = Photo
    template_name = "stream.html"


class UploadPhoto(CreateView):
    model = Photo
    template_name = "upload_photo.html"


class CreateAlbum(CreateView):
    model = Album
    template_name = "create_album"


@login_required
def library_view(request, *args, **kwargs):
    print kwargs
    return render(request, 'library.html', {})
