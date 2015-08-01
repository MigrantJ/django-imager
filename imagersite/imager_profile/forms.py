from django import forms
from .models import ImagerProfile


class ProfileSettingsForm(forms.ModelForm):
    first_name = forms.CharField(label='First Name', max_length=36)
    last_name = forms.CharField(label='Last Name', max_length=36)
    email = forms.EmailField(label='Email')

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(ProfileSettingsForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].initial = self.instance.user.first_name
        self.fields['last_name'].initial = self.instance.user.last_name
        self.fields['email'].initial = self.instance.user.email

    # def save(self, *args, **kwargs):
    #     super(ProfileSettingsForm, self).save(*args, **kwargs)
    #     self.instance.profile.address = self.cleaned_data.get('address')
    #     self.instance.profile.save()

    class Meta:
        model = ImagerProfile
        fields = ['address', 'fav_camera', 'photo_type', 'url']
