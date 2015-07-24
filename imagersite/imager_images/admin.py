from django.contrib import admin
from .models import Photos, Album


# class CategoryUser(admin.ModelAdmin):
#     list_display = ['email', 'user_id']

#     class Meta:
#         model = Photos

admin.site.register(Photos)
admin.site.register(Album)
