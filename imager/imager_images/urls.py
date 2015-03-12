from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from imager_images.views import StreamView, UploadPhoto, CreateAlbum


urlpatterns = patterns('',
                       url(r'^(?P<pk>\d+)$',
                           login_required(StreamView.as_view(
                               template_name='stream.html')),
                           name='stream'),
                       url(r'library/(?P<pk>\d+)$',
                           'imager_images.views.library_view',
                           name='library'),
                       url(r'^upload_photo$',
                           login_required(UploadPhoto.as_view(
                               template_name='upload_photo.html')),
                           name='upload_photo'),
                       url(r'^create_album$',
                           login_required(CreateAlbum.as_view(
                               template_name='create_album.html')),
                           name='create_album'),
                       )
