from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='profile'),
    url(r'^images/library', views.PhotoListView.as_view(), name='library'),
    url(r'^images/albums', views.AlbumListView.as_view(), name='albums'),
    url(
        r'^images/albums/(?P<album_id>\d+)',
        views.AlbumDetailListView.as_view(),
        name='albums_detail'),
    url(
        r'^images/photos/(?P<pk>\d+)$',
        views.PhotoDetailView.as_view(),
        name='photo_detail'),
]
