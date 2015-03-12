from django.shortcuts import render
from django.views.generic import ListView
from imager_images.models import Photo
from django.contrib.auth.decorators import login_required
#from imager_users.forms import ImagerProfileEditForm # to override form


@login_required
class StreamView(ListView):
    model = Photo
    template_name = "stream.html"


@login_required
def library_view(request, *args, **kwargs):
    print kwargs
    return render(request, 'library.html', {})
