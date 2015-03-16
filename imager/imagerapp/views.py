from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import DetailView
from imagerapp.models import ImagerProfile
from imagerapp.forms import ProfileForm
from django.core.urlresolvers import reverse

# from django.template import RequestContext, loader
# from django.views.generic.edit import FormView
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
#from imager_users.forms import ImagerProfileEditForm # to override form
# from django.views.decorators.http import require_http_methods
# from django.core.context_processors import csrf


class ImagerProfileDetailView(DetailView):
    model = ImagerProfile
    template_name = "profile_detail.html"


def profile_update_view(request, *args, **kwargs):
    profile = ImagerProfile.objects.get(pk=kwargs['pk'])
    user = profile.user
    # import pdb; pdb.set_trace()
    if request.method == 'POST':
        # For submission of form for updating information...
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.email = form.cleaned_data.get('email')
            user.save()
            return HttpResponseRedirect(
                reverse(
                    'profile_detail',
                    kwargs={'pk': request.user.profile.pk}
                ))
    else:
        # For populating a form when a user navigates to page
        # using the edit link in the profile detail page...
        initial = {'first_name': user.first_name,
                   'last_name': user.last_name,
                   'email': user.email,
                   }

        form = ProfileForm(instance=profile, initial=initial)
    return render(request, 'profile_update.html', {'form': form})
