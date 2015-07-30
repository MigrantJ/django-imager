from .models import Photos
from django.views.generic import TemplateView
from django.views.generic import FormView
from .forms import AlbumForm, PhotoForm


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        p = Photos.objects.filter(published='public').order_by('?').first()
        context = super(IndexView, self).get_context_data(**kwargs)
        context['photo'] = p
        return context


class AlbumFormView(FormView):
    template_name = 'album_form.html'
    form_class = AlbumForm
    success_url = '/profile/'

    def form_valid(self, form):
        pass


class PhotoFormView(FormView):
    template_name = 'photo_form.html'
    form_class = PhotoForm
    success_url = 'images/photo_form/'

    def form_valid(self, form):
        pass
