from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from imager_images.views import StreamView, UploadPhoto, CreateAlbum, EditPhoto, EditAlbum


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
                       url(r'^edit_photo/(?P<pk>\d+)$', login_required(EditPhoto.as_view(
                               template_name='edit_photo.html')),
                           name='edit_photo'
                           ),
                       url(r'^create_album$',
                           login_required(CreateAlbum.as_view(
                               template_name='create_album.html')),
                           name='create_album'),
                       url(r'^edit_album/(?P<pk>\d+)$', login_required(EditAlbum.as_view(
                               template_name='edit_album.html')),
                           name='edit_album'
                           ),
                       )
