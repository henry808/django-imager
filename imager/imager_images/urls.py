from django.conf.urls import patterns, url
from imager_images.views import StreamView


urlpatterns = patterns('',
          url(r'^(?P<pk>\d+)$', StreamView.as_view(
          template_name='stream.html'),
          name='stream'),
)