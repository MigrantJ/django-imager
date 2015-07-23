from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class ImagerProfile(models.Model):
    PHOTO_TYPES = (
        ('N', 'Nature Photography'),
        ('P', 'Paranormal Photography'),
        ('A', 'Aerial Photography'),
        ('B', 'Black and White Photography'),
        ('F', 'Forensic Photography')
    )
    user = models.OneToOneField(
        User,
        related_name="profile",
        null=False
    )
    fav_camera = models.CharField(max_length=256)
    address = models.TextField()
    url = models.URLField()
    photo_type = models.CharField(max_length=1,
                                  choices=PHOTO_TYPES,
                                  default='N')
    objects = models.Manager()
    active = ActiveProfileManager()

    def __str__(self):
        return self.user.get_full_name() or self.user.username

    @property
    def is_active(self):
        return self.user.is_active


class ActiveProfileManager(models.Manager):
    def get_queryset(self):
        return super(ActiveProfileManager, self).get_queryset()\
            .filter(user__is_active=True)
