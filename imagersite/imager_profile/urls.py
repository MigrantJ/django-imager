from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='profile'),
    url(r'^images/library$', views.PhotoListView.as_view(), name='library'),
    url(r'^images/albums$', views.AlbumListView.as_view(), name='albums'),
    url(
        r'^images/albums/(?P<pk>\d+)$',
        views.AlbumDetailListView.as_view(),
        name='albums_detail'),
    url(
        r'^images/photos/(?P<pk>\d+)$',
        views.PhotoDetailView.as_view(),
        name='photo_detail'),
    url(
        r'^settings/$',
        views.ProfileSettingsView.as_view(),
        name='profile_settings'),
    url(
        r'^images/photos/(?P<pk>\d+)/detect$',
        views.PhotoDetailView.as_view(detect='hello'),
        name='detect_faces'),
    url(r'^photo/(?P<pk>\d+)/face/edit/$',
        views.FaceEditView.as_view(),
        name='edit_face')
]
