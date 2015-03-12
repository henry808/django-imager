from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext, loader
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView
from django.contrib.auth.decorators import login_required
from imagerapp.models import ImagerProfile
from django.contrib.auth.models import User
#from imager_users.forms import ImagerProfileEditForm # to override form


class ImagerProfileDetailView(DetailView):
    model = ImagerProfile
    template_name = "profile_detail.html"


class ImagerProfileUpdateView(UpdateView):
    model = ImagerProfile

    template_name = "profile_update.html"
