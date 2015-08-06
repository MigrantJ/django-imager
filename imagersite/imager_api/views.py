from django.shortcuts import render
from rest_framework import viewsets
from imager_images.models import Photos
from serializers import PhotoSerializer


class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photos.objects.all()
    serializer_class = PhotoSerializer
