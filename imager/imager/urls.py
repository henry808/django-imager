from django.conf.urls import patterns, include, url
from django.contrib import admin
from settings import MEDIA_ROOT
from registration.backends.simple.views import RegistrationView

urlpatterns = patterns('',
    url(r'^$', 'imager.views.home', name='home'),
    #url(r'^imagerapp/', include(imagerapp.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                 {'document_root': MEDIA_ROOT}),
)
