from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete

from .models import ImagerProfile


@receiver(post_save)
def create_user_profile(sender, **kwargs):
    instance = kwargs.get('instance')
    instance.profile = ImagerProfile()
    instance.profile.save()


@receiver(post_delete)
def del_user_profile(sender, **kwargs):
    instance = kwargs.get('instance')
    instance.user.delete()
