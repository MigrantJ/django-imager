from django import forms
from .models import Photos, Album


class AlbumForm(forms.Form):
    title = forms.CharField(max_length=128, help_text='Enter Album Name')
    description = forms.CharField(
        max_length=128,
        help_text='Enter Description'
    )

    class Meta:
        model = Album
        fields = ['title', 'description', 'published', 'photos', 'cover']


class PhotoForm(forms.Form):
    title = forms.CharField(max_length=128, help_text='Enter Album Name')
    description = forms.CharField(
        max_length=496,
        help_text='Enter Description'
    )

    class Meta:
        model = Photos
        fields = ['image', 'title', 'description', 'published']
