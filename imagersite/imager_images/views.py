from django.shortcuts import render
from .models import Photos
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        p = Photos.objects.filter(published='public').order_by('?').first()
        context = {
            'photo': p
        }
        return render(request, self.template_name, context=context)
