from django import forms
from imagerapp.models import ImagerProfile


class ProfileForm(forms.Form):
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    phone = forms.IntegerField(required=False)
    email = forms.CharField()
    picture = forms.ImageField(required=False)
    birthday = forms.DateField()

    name_privacy = forms.MultipleChoiceField(choices=ImagerProfile.PRIVACY_CHOICES, widget=forms.RadioSelect)
    phone_privacy = forms.MultipleChoiceField(choices=ImagerProfile.PRIVACY_CHOICES, widget=forms.RadioSelect)
    email_privacy = forms.MultipleChoiceField(choices=ImagerProfile.PRIVACY_CHOICES, widget=forms.RadioSelect)
    pic_privacy = forms.MultipleChoiceField(choices=ImagerProfile.PRIVACY_CHOICES, widget=forms.RadioSelect)
    birthday_privacy = forms.MultipleChoiceField(choices=ImagerProfile.PRIVACY_CHOICES, widget=forms.RadioSelect)
