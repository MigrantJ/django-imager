from django.shortcuts import render
from imager_images.models import Photos
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        p = Photos.objects.filter(published='public').order_by('?').first()
        context = super(IndexView, self).get_context_data(**kwargs)
        context['photo'] = p
        return context

# This is for getting the user pref fields on the profile page via context.
# user.profile._meta.get_fields()
