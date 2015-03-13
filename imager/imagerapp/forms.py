from django import forms
from django.forms import Form
from django.forms.models import inlineformset_factory
# from django.contrib.auth.models import User
from imagerapp.models import ImagerProfile


# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields =  ['first_name',
#                    'last_name',
#                    'email']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = ImagerProfile
        fields = ['phone',
                  'picture',
                  'birthday',
                  'name_privacy',
                  'phone_privacy',
                  'email_privacy',
                  'pic_privacy',
                  'birthday_privacy']

    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    email = forms.CharField()

# ProfileFormSet = inlineformset_factory(User, ImagerProfile)

    # cleaned_data = super(Form, self).clean()
    # picture = forms.ImageField(required=False)
    # birthday = forms.DateField()

    # name_privacy = forms.MultipleChoiceField(choices=ImagerProfile.PRIVACY_CHOICES, widget=forms.RadioSelect)
    # phone_privacy = forms.MultipleChoiceField(choices=ImagerProfile.PRIVACY_CHOICES, widget=forms.RadioSelect)
    # email_privacy = forms.MultipleChoiceField(choices=ImagerProfile.PRIVACY_CHOICES, widget=forms.RadioSelect)
    # pic_privacy = forms.MultipleChoiceField(choices=ImagerProfile.PRIVACY_CHOICES, widget=forms.RadioSelect)
    # birthday_privacy = forms.MultipleChoiceField(choices=ImagerProfile.PRIVACY_CHOICES, widget=forms.RadioSelect)
