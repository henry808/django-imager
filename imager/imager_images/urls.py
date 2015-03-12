from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from imager_images.views import StreamView


urlpatterns = patterns('',
                       url(r'^(?P<pk>\d+)$',
                           login_required(StreamView.as_view(
                               template_name='stream.html')),
                           name='stream'),
                       url(r'library/(?P<pk>\d+)$',
                           'imager_images.views.library_view',
                           name='library')
                       )
