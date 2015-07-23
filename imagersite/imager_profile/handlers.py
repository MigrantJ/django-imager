from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User
from .models import ImagerProfile


@receiver(post_save, sender=User)
def create_user_profile(sender, **kwargs):
    instance = kwargs.get('instance')
    if not instance or kwargs.get('raw', False):
        return
    try:
        instance.profile
    except:
        instance.profile = ImagerProfile()
        instance.profile.save()


@receiver(post_delete, sender=ImagerProfile)
def del_user_profile(sender, **kwargs):
    instance = kwargs.get('instance')
    if not instance:
        return
    try:
        instance.user.delete()
    except:
        pass
