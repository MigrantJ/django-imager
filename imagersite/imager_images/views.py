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

    def get_form(self, form_class=AlbumForm):
        try:
            album = Album.objects.get(user=self.request.user)
            return AlbumForm(instance=album, **self.get_form_kwargs())
        except Album.DoesNotExist:
            return AlbumForm(**self.get_form_kwargs())

    def get_form_kwargs(self):
        kwargs = super(AlbumFormView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        album = form.save(commit=False)
        album.user = self.request.user
        album.save()
        return super(AlbumFormView, self).form_valid(album)


class PhotoFormView(FormView):
    template_name = 'photo_form.html'
    form_class = PhotoForm
    success_url = '/profile/images/library'

    def get_form(self, form_class=PhotoForm):
        try:
            photo = Photos.objects.get(user=self.request.user)
            return PhotoForm(instance=photo, **self.get_form_kwargs())
        except Photos.DoesNotExist:
            return PhotoForm(**self.get_form_kwargs())

    def form_valid(self, form):
        photo = form.save(commit=False)
        photo.user = self.request.user
        photo.save()
        return super(PhotoFormView, self).form_valid(photo)
