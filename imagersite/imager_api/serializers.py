from imager_images.models import Photos
from rest_framework import serializers


class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Photos
        fields = ('title',
                  'description',
                  'date_uploaded',
                  'date_modified',
                  'date_published',
                  'published')
