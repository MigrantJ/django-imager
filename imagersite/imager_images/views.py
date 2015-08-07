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
