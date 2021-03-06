from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.gis.db import models as geomodels

PUBLISHED_CHOICES = (
    ('private', 'private'),
    ('shared', 'shared'),
    ('public', 'public')
)


@python_2_unicode_compatible
class Photos(models.Model):
    image = models.ImageField(upload_to='photo_files/%Y-%m-%d')
    user = models.ForeignKey(
        User,
        null=False
    )
    title = models.CharField(max_length=256)
    description = models.TextField()
    date_uploaded = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)
    date_published = models.DateField(auto_now_add=True)

    published = models.CharField(max_length=256,
                                 choices=PUBLISHED_CHOICES,
                                 default='private')

    location = geomodels.PointField(geography=True, null=True, blank=True)
    objects = geomodels.GeoManager()

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class Album(models.Model):
    user = models.ForeignKey(
        User,
        null=False
    )
    photos = models.ManyToManyField(
        Photos,
        related_name='albums',
        blank=True
    )
    cover = models.ForeignKey(
        Photos,
        related_name='cover_for',
        null=True,
        blank=True
    )
    title = models.CharField(max_length=256)
    description = models.TextField()
    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)
    date_published = models.DateField(auto_now_add=True)
    published = models.CharField(max_length=256,
                                 choices=PUBLISHED_CHOICES,
                                 default='private')

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class Face(models.Model):
    photo = models.ForeignKey(
        Photos,
        related_name='faces',
        null=False,
    )
    x = models.IntegerField()
    y = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()
    name = models.CharField(max_length=256)

    def __str__(self):
        return 'Face: ' + self.photo.title + ' : ' + self.name
