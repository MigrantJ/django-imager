from django.views.generic import TemplateView, ListView, DetailView, FormView
from imager_images.models import Photos, Album
from .models import ImagerProfile
# from django.contrib.auth.models import User
from .forms import ProfileSettingsForm


class IndexView(TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        try:
            pho = Photos.objects.filter(
                user=self.request.user).order_by('?').first()
            alb = Album.objects.filter(
                user=self.request.user).order_by('?').first()
            context = super(IndexView, self).get_context_data(**kwargs)
            context['photo'] = pho
            context['album'] = alb
        except TypeError:
            context = super(IndexView, self).get_context_data(**kwargs)

        return context


class PhotoListView(ListView):
    template_name = 'photos_list.html'
    model = Photos

    def get_queryset(self):
        photos = None
        try:
            photos = Photos.objects.filter(
                user=self.request.user)
        except TypeError:
            pass

        return photos


class AlbumListView(ListView):
    template_name = 'album_list.html'
    model = Album

    def get_queryset(self):
        albums = None
        try:
            albums = Album.objects.filter(user=self.request.user)
        except TypeError:
            pass

        return albums


class AlbumDetailListView(ListView):
    template_name = 'photos_list.html'
    model = Album

    def get_queryset(self):
        photos = None
        try:
            photos = Photos.objects.filter(
                user=self.request.user,
                albums__id=self.kwargs['pk'])
        except TypeError:
            pass

        return photos


class PhotoDetailView(DetailView):
    template_name = 'photos_detail.html'
    model = Photos

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        return context


class ProfileSettingsView(FormView):
    template_name = 'profile_settings.html'
    form_class = ProfileSettingsForm
    success_url = '/profile/settings'

    # def get_form_kwargs(self):
    #     kwargs = super(ProfileSettingsView, self).get_form_kwargs()
    #     kwargs['request'] = self.request
    #     return kwargs
    #
    # def form_valid(self, form):
    #     user = form.save(commit=False)
    #     user.user = self.request.user
    #     user.save()
    #     return super(ProfileSettingsView, self).form_valid()
