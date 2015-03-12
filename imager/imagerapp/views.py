from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext, loader
from django.views.generic import DetailView
from django.views.generic.edit import FormView
from django.contrib.auth.decorators import login_required
from imagerapp.models import ImagerProfile
from django.contrib.auth.models import User
from imagerapp.forms import ProfileForm
#from imager_users.forms import ImagerProfileEditForm # to override form


class ImagerProfileDetailView(DetailView):
    model = ImagerProfile
    template_name = "profile_detail.html"


# class ImagerProfileUpdateView(FormView):
#     template_name = "profile_update.html"
#     instance = {'first_name': 'the first one'}
#     form_class = ProfileForm
#     success_url = 'profile_detail'


@login_required
def profile_update_view(request, *args, **kwargs):
    profile = ImagerProfile.objects.get(pk=kwargs['pk'])
    user = profile.user
    initial = {'first_name': user.first_name,
               'last_name': user.last_name,
               'phone': profile.phone,
               'email': user.email,
               'birthday': profile.birthday,
               'picture': profile.picture,

               'name_privacy': profile.name_privacy,
               'email_privacy': profile.email_privacy,
               'birthday_privacy': profile.birthday_privacy,
               'pic_privacy': profile.pic_privacy,
               'phone_privacy': profile.phone_privacy}

    form = ProfileForm(initial=initial)
    return render(request, 'profile_update.html', {'form': form})