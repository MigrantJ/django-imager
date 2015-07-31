from django import forms
from .models import Photos, Album


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['title', 'description', 'published', 'photos', 'cover']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(AlbumForm, self).__init__(*args, **kwargs)
        self.fields['photos'].queryset = Photos.objects.filter(
            user=self.request.user)


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photos
        fields = ['image', 'title', 'description', 'published']
