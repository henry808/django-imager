from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from imager_images.models import Photo, Album
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
#from imager_users.forms import ImagerProfileEditForm # to override form


class StreamView(ListView):
    model = Photo
    template_name = "stream.html"


class UploadPhoto(CreateView):
    model = Photo
    template_name = "upload_photo.html"
    fields = ['picture', 'title', 'description', 'published']

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = form_class(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.user = request.user
            photo.save()
            return HttpResponseRedirect(
                reverse(
                    'library',
                    kwargs={'pk': request.user.profile.pk}
                ))

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
            return HttpResponseRedirect(
                reverse(
                    'library',
                    kwargs={'pk': instance.user.profile.pk}
                ))

        return self.render_to_response({'form': form})


class CreateAlbum(CreateView):
    model = Album
    template_name = "create_album"

    fields = ['title',
              'photos',
              'cover_photo',
              'description',
              'published']

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = form_class(request.POST)
        if form.is_valid():
            album = form.save(commit=False)
            album.user = request.user
            album.save()
            return HttpResponseRedirect(
                reverse(
                    'library',
                    kwargs={'pk': request.user.profile.pk}
                ))

        return self.render_to_response({'form': form})

    def get_form(self, form_class):
        form = super(EditAlbum, self).get_form(form_class)
        filter1 = Photo.objects.filter(user=self.request.user)
        form.fields['photos'].queryset = filter1
        form.fields['cover_photo'].queryset = filter1
        return form


class EditAlbum(UpdateView):
    model = Album
    template_name = "edit_album.html"
    fields = ['title',
              'photos',
              'cover_photo',
              'description',
              'published']

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        instance = Album.objects.get(pk=kwargs['pk'])
        form = form_class(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(
                reverse(
                    'library',
                    kwargs={'pk': instance.user.profile.pk}
                ))

        return self.render_to_response({'form': form})

    def get_form(self, form_class):
        form = super(EditAlbum, self).get_form(form_class)
        filter1 = Photo.objects.filter(user=self.request.user)
        form.fields['photos'].queryset = filter1
        form.fields['cover_photo'].queryset = filter1
        return form


@login_required
def library_view(request, *args, **kwargs):
    print kwargs
    return render(request, 'library.html', {})
