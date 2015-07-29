from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='profile'),
    url(r'^images/library', views.PhotoListView.as_view(), name='library'),
    url(r'^images/albums', views.AlbumListView.as_view(), name='albums'),
    url(r'^images/albums/', views.AlbumDetailListView.as_view(), name='albums_detail'),
]
