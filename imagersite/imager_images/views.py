from .models import Photos, Album
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, FormView
from .forms import AlbumForm, PhotoForm


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        try:
            p = Photos.objects.filter(published='public').order_by('?').first()
            context = super(IndexView, self).get_context_data(**kwargs)
            context['photo'] = p
        except TypeError:
            context = super(IndexView, self).get_context_data(**kwargs)

        return context


class PhotoCreateView(CreateView):
    model = Photos
    fields = ['image', 'title', 'description', 'published', 'location']
    template_name = 'photo_form.html'
    success_url = '/profile/images/library'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PhotoCreateView, self).form_valid(form)


class PhotoEditView(UpdateView):
    model = Photos
    fields = ['image', 'title', 'description', 'published', 'location']
    template_name = 'photo_form.html'
    success_url = '/profile/images/library'


class AlbumCreateView(CreateView):
    model = Album
    fields = ['title', 'description', 'published', 'photos', 'cover']
    template_name = 'album_form.html'
    success_url = '/profile/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AlbumCreateView, self).form_valid(form)


class AlbumEditView(UpdateView):
    model = Album
    fields = ['title', 'description', 'published', 'photos', 'cover']
    template_name = 'album_form.html'
    success_url = '/profile/'
