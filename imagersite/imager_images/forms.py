from django import forms
from django.contrib.gis import forms as geoforms
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


class GeoForm(forms.ModelForm):
    location = geoforms.PointField(
        widget=geoforms.OpenLayersWidget(
            attrs={'map_width': 300, 'map_height': 300}))

    class Meta:
        model = Photos
        fields = ['location']
