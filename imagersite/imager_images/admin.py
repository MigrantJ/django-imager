from django.contrib import admin
from .models import Photos


# class CategoryUser(admin.ModelAdmin):
#     list_display = ['email', 'user_id']

#     class Meta:
#         model = Photos

admin.site.register(Photos)
