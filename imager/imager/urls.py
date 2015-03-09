from django.conf.urls import patterns, include, url
from django.contrib import admin
import imagerapp

urlpatterns = patterns('',
    url(r'^$', 'imager.views.home', name='home'),
    #url(r'^imagerapp/', include(imagerapp.urls)),
    url(r'^admin/', include(admin.site.urls)),
)
