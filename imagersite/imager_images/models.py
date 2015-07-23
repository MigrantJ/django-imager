from django.db import models


class Photos(models.Model):
    image = models.ImageField(upload_to='photo_files/%Y-%m-%d')
