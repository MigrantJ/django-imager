from .models import Photos, Album
from django.views.generic import TemplateView
from django.views.generic import FormView
from .forms import AlbumForm, PhotoForm, GeoForm


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
            album = Album.objects.get(
                user=self.request.user, pk=self.kwargs['pk'])
            return AlbumForm(instance=album, **self.get_form_kwargs())
        except (KeyError, Album.DoesNotExist):
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
    form_classes = {'photo': PhotoForm, 'location': GeoForm}
    success_url = '/profile/images/library'

    def get_photo_form(self, form_class=PhotoForm):
        try:
            photo = Photos.objects.get(
                user=self.request.user,
                pk=self.kwargs['pk']
            )
            return PhotoForm(instance=photo, **self.get_form_kwargs())
        except (KeyError, Photos.DoesNotExist):
            return PhotoForm(**self.get_form_kwargs())

    def get_location_form(self, form_class=GeoForm):
        try:
            photo = Photos.objects.location.get(
                user=self.request.user,
                pk=self.kwargs['pk']
            )
            return GeoForm(instance=photo, **self.get_form_kwargs())
        except (KeyError, Photos.DoesNotExist):
            return GeoForm(**self.get_form_kwargs())

    # def get_form_kwargs(self):
    #     kwargs = super(PhotoFormView, self).get_form_kwargs()
    #     kwargs['request'] = self.request
    #     return kwargs

    def photo_form_valid(self, form):
        photo = form.save(commit=False)
        photo.user = self.request.user
        photo.save()
        return super(PhotoFormView, self).photo_form_valid(photo)

    def location_form_valid(self, form):
        location = form.save(commit=False)
        location.user = self.request.user
        location.save()
        return super(PhotoFormView, self).location_form_valid(location)
