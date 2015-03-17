from django.conf.urls import patterns, include, url
from django.contrib import admin
# from registration.backends.simple.views import RegistrationView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    url(r'^$', 'imager.views.home', name='home'),
    #url(r'^imagerapp/', include(imagerapp.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^profile/', include('imagerapp.urls')),
    url(r'^images/', include('imager_images.urls')),
    # url(r'^static/(?P<path>images/.*)$', 'django.views.static.serve',
    #              {'document_root': settings.STATIC_ROOT}),
)

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)