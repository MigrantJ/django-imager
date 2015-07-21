from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete


class ImagerProfile(models.Model):
    PHOTO_TYPES = (
        ('N', 'Nature Photography'),
        ('P', 'Paranormal Photography'),
        ('A', 'Aerial Photography'),
        ('B', 'Black and White Photography'),
        ('F', 'Forensic Photography')
    )
    user = models.OneToOneField(User, unique=True)
    fav_camera = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
    url = models.URLField()
    photo_type = models.CharField(max_length=1,
                                  choices=PHOTO_TYPES,
                                  default='N')
    active = models.BooleanField()

    def __str__(self):
        return 'ImagerProfile: ' + self.user.username

    def __unicode__(self):
        return unicode('ImagerProfile: ' + self.user.username)

    @property
    def is_active(self):
        return self.active


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        ImagerProfile.objects.create(user=instance)


def delete_user_profile(sender, instance, created, **kwargs):
    pass

post_save.connect(create_user_profile, sender=User)
post_delete.connect(delete_user_profile, sender=User)
