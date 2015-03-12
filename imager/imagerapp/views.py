from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext, loader
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from imagerapp.models import ImagerProfile
#from imager_users.forms import ImagerProfileEditForm # to override form


@login_required
class ImagerProfileDetailView(DetailView):
    model = ImagerProfile
    template_name = "profile_detail.html"