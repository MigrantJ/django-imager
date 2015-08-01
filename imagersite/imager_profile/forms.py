from django import forms
from .models import ImagerProfile
from django.contrib.auth.models import User


class UserSettingsForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class ProfileSettingsForm(UserSettingsForm):
    # class Meta:
    #     model = ImagerProfile
        # fields = []

    def __init__(self, *args, **kwargs):
        super(ProfileSettingsForm, self).__init__(*args, **kwargs)
