from django.views.generic import TemplateView, ListView, DetailView
from imager_images.models import Photos, Album


class IndexView(TemplateView):
    template_name = 'profile.html'
    
    def get_context_data(self, **kwargs):
        pho = Photos.objects.filter(published='public').order_by('?').first()
        alb = Album.objects.all().order_by('?').first()
        context = super(IndexView, self).get_context_data(**kwargs)
        context['photo'] = pho
        context['album'] = alb
        return context


class PhotoListView(ListView):
    template_name = 'photos_list.html'
    model = Photos

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        return context


class AlbumListView(ListView):
    template_name = 'album_list.html'
    model = Album

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        return context


class AlbumDetailListView(ListView):
    template_name = 'photos_list.html'
    model = Album

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        return context


class PhotoDetailView(DetailView):
    template_name = 'photos_detail.html'
    model = Photos

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        return context
