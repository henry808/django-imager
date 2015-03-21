from django.conf.urls import patterns, include, url
from django.contrib import admin
from imagerapp.views import ImagerProfileDetailView
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('',
                       url(r'^(?P<pk>\d+)$',
                           login_required(ImagerProfileDetailView.as_view(
                               template_name='profile_detail.html')),
                           name='profile_detail'),
                       url(r'^update/(?P<pk>\d+)$',
                           'imagerapp.views.profile_update_view',
                           name='profile_update'),
                       # url(r'^update_action/(?P<pk>\d+)$',
                       #     'imagerapp.views.profile_update_view',
                       #     name='profile_update_action'),
)