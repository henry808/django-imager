from django.conf.urls import patterns, include, url
from django.contrib import admin
from imagerapp.views import ImagerProfileDetailView, ImagerProfileUpdateView
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('',
                       url(r'^(?P<pk>\d+)$',
                           login_required(ImagerProfileDetailView.as_view(
                               template_name='profile_detail.html')),
                           name='profile_detail'),
                       url(r'^update/(?P<pk>\d+)$',
                           login_required(ImagerProfileUpdateView.as_view(
                               template_name='profile_update.html')),
                           name='profile_update'),
    # Examples:

    # url(r'^$', 'imager.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
)