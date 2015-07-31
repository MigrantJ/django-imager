from .models import Photos, Album
from django.views.generic import TemplateView
from django.views.generic import FormView
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


class AlbumFormView(FormView):
    template_name = 'album_form.html'
    form_class = AlbumForm
    success_url = '/profile/'

    def get_form_kwargs(self):
        kwargs = super(AlbumFormView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        album = form.save()
        album.objects.create(
            user=form.cleaned_data['user'],
            title=form.cleaned_data['title'],
            description=form.cleaned_data['description'],
            published=form.cleaned_data['published'],
            photos=form.cleaned_data['photos'],
            cover=form.cleaned_data['cover'],
        )
        return super(AlbumFormView, self).form_valid(album)


class PhotoFormView(FormView):
    template_name = 'photo_form.html'
    form_class = PhotoForm
    success_url = 'images/photo_form/'

    def form_valid(self, form):
        # photo = Photos.objects.create()
        pass
