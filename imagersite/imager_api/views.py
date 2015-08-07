from django.shortcuts import render
from rest_framework import viewsets
from imager_images.models import Photos
from serializers import PhotoSerializer
from django.db.models import Q


class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photos.objects.all()
    serializer_class = PhotoSerializer

    def get_queryset(self):
        qs = super(PhotoViewSet, self).get_queryset()
        if self.request.user.is_anonymous():
            qs = qs.filter(published='public')
        else:
            is_mine = Q(user=self.request.user)
            is_public = Q(published='public')
            qs = qs.filter(is_mine | is_public).distinct()
        return qs
