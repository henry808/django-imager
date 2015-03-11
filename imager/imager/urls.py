from django.conf.urls import patterns, include, url
from django.contrib import admin
# from registration.backends.simple.views import RegistrationView
from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = patterns('',
    url(r'^$', 'imager.views.home', name='home'),
    #url(r'^imagerapp/', include(imagerapp.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
                 {'document_root': settings.MEDIA_ROOT}),
    # url(r'^static/(?P<path>images/.*)$', 'django.views.static.serve',
    #              {'document_root': settings.STATIC_ROOT}),
)   # + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
   urlpatterns += patterns('django.contrib.staticfiles.views',
       url(r'^static/(?P<path>.*)$', 'serve'),
   )