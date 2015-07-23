from django.db import models
from django.contrib.auth.models import User

PUBLISHED_CHOICES = (
    ('private', 'private'),
    ('shared', 'shared'),
    ('public', 'public')
)


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

    published = models.CharField(max_length=1,
                                 choices=PUBLISHED_CHOICES,
                                 default='private')


class Album(models.Model):
    user = models.ForeignKey(
        User,
        null=False
    )
    photos = models.ManyToManyField(
        Photos,
        limit_choices_to={'user': user}
    )
    cover = models.ForeignKey(
        Photos,
    )
    title = models.CharField(max_length=256)
    description = models.TextField()
    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)
    date_published = models.DateField(auto_now_add=True)
    published = models.CharField(max_length=1,
                                 choices=PUBLISHED_CHOICES,
                                 default='private')
