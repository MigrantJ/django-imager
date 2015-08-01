from django import forms
from .models import ImagerProfile
# from django.contrib.auth.models import User


class ProfileSettingsForm(forms.ModelForm):
    class Meta:
        model = ImagerProfile
        fields = ['address']
