from django.shortcuts import render
from .models import Photos
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        p = Photos.objects.filter(published='public').order_by('?').first()
        context = super(IndexView, self).get_context_data(**kwargs)
        context['photo'] = p
        return context
