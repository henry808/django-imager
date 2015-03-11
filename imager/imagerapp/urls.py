from django.conf.urls import patterns, include, url
from django.contrib import admin
from imagerapp.views import ImagerProfileDetailView

urlpatterns = patterns('',
          url(r'^(?P<pk>\d+)$', ImagerProfileDetailView.as_view(
          template_name='profile_detail.html'),
          name='profile_detail'),
    # Examples:

    # url(r'^$', 'imager.views.home', name='home'),
    # # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
)