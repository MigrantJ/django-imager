from django.shortcuts import render
from .models import Photos
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        context = {
            'photo': Photos.objects.filter(published='public').first()
        }
        return render(request, self.template_name, context=context)
