from django import forms
from .models import ImagerProfile
# from django.contrib.auth.models import User


class ProfileSettingsForm(forms.ModelForm):
    first_name = forms.CharField(label='First Name', max_length=256)

    def __init__(self, *args, **kwargs):
        super(ProfileSettingsForm, self).__init__(*args, **kwargs)
        self.fields['first_name'] = self.instance.user.first_name

    # def save(self, *args, **kwargs):
    #     super(ProfileSettingsForm, self).save(*args, **kwargs)
    #     self.instance.profile.address = self.cleaned_data.get('address')
    #     self.instance.profile.save()

    class Meta:
        model = ImagerProfile
        fields = ['user']
