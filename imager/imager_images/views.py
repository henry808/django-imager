from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from imager_images.models import Photo, Album
from django.contrib.auth.decorators import login_required
#from imager_users.forms import ImagerProfileEditForm # to override form


class StreamView(ListView):
    model = Photo
    template_name = "stream.html"


class UploadPhoto(CreateView):
    model = Photo
    template_name = "upload_photo.html"
    fields = ['picture', 'title', 'description', 'published']

    def post(self, request, *args, **kwargs):
        import pdb; pdb.set_trace()
        form_class = self.get_form_class()
        form = form_class(request.POST)
        if form.is_valid():
            form.save()

        return self.render_to_response({'form': form})


class EditPhoto(UpdateView):
    model = Photo
    template_name = "edit_photo.html"
    fields = ['title', 'description', 'published']

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        instance = Photo.objects.get(pk=kwargs['pk'])
        form = form_class(request.POST, instance=instance)
        if form.is_valid():
            form.save()

        return self.render_to_response({'form': form})


class CreateAlbum(CreateView):
    model = Album
    template_name = "create_album"
    fields = ['user', 'title']

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        # instance = Album.objects.get(pk=kwargs['pk'])
        import pdb; pdb.set_trace()
        form = form_class(request.POST)
        if form.is_valid():
            form.save()

        return self.render_to_response({'form': form})


class EditAlbum(UpdateView):
    model = Album
    template_name = "edit_album.html"
    fields = ['title', 'description', 'published']

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        instance = Album.objects.get(pk=kwargs['pk'])
        form = form_class(request.POST, instance=instance)
        if form.is_valid():
            form.save()

        import pdb; pdb.set_trace()
        return self.render_to_response({'form': form})


@login_required
def library_view(request, *args, **kwargs):
    print kwargs
    return render(request, 'library.html', {})
