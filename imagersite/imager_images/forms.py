from django import forms
from .models import Photos, Album


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['title', 'description', 'published', 'photos', 'cover']

    def __init__(self, *args, **kwargs):
        super(AlbumForm, self).__init__(*args, **kwargs)


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photos
        fields = ['image', 'title', 'description', 'published', 'location']
