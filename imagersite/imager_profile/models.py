from django.db import models
from django.contrib.auth.models import User


class ImagerProfile(models.Model):
    PHOTO_TYPES = (
        ('N', 'Nature Photography'),
        ('P', 'Paranormal Photography'),
        ('A', 'Aerial Photography'),
        ('B', 'Black and White Photography'),
        ('F', 'Forensic Photography')
    )
    user = models.OneToOneField(User)
    fav_camera = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
    url = models.URLField()
    photo_type = models.CharField(max_length=1,
                                  choices=PHOTO_TYPES,
                                  default='N')
    active = models.BooleanField()

    @property
    def is_active(self):
        return self.active
