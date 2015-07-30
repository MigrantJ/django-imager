from django.views.generic import TemplateView, ListView, DetailView
from imager_images.models import Photos, Album


class IndexView(TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        pho = Photos.objects.filter(
            published='public',
            user=self.request.user).order_by('?').first()
        alb = Album.objects.filter(
            user=self.request.user).order_by('?').first()
        context = super(IndexView, self).get_context_data(**kwargs)
        context['photo'] = pho
        context['album'] = alb
        return context


class PhotoListView(ListView):
    template_name = 'photos_list.html'
    model = Photos

    def get_queryset(self):
        return Photos.objects.filter(
            published='public',
            user=self.request.user)


class AlbumListView(ListView):
    template_name = 'album_list.html'
    model = Album

    def get_queryset(self):
        return Album.objects.filter(user=self.request.user)


class AlbumDetailListView(ListView):
    template_name = 'photos_list.html'
    model = Album

    def get_queryset(self):
        return Photos.objects.filter(
            published='public',
            user=self.request.user,
            albums__id=self.kwargs['pk'])


class PhotoDetailView(DetailView):
    template_name = 'photos_detail.html'
    model = Photos

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        return context
