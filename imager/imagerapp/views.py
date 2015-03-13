from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404, HttpResponseForbidden
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
    # import pdb; pdb.set_trace()
    if request.method == 'POST':
        # For submission of form for updating information...
        form = ProfileForm(instance=profile, initial=request.POST)
        if form.is_valid():
            form = form.clean()
            form.save()
        else:
            return render(request, 'profile_update.html', {'form': form})

        user.first_name = form.fields.get('first_name')
        user.last_name = form.fields.get('last_name')
        user.email = form.fields.get('email')
        user.save()
    else:
        # For populating a form when a user navigates to page
        # using the edit link in the profile detail page...
        initial = {'first_name': user.first_name,
                   'last_name': user.last_name,
                   'email': user.email,
                   }

        form = ProfileForm(instance=profile, initial=initial)
    return render(request, 'profile_update.html', {'form': form})