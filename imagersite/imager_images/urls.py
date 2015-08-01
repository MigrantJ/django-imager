from django.conf.urls import url
import views

urlpatterns = [
    url(r'^home/$', views.IndexView.as_view(), name='index'),
    url(r'^photo/add/$', views.PhotoFormView.as_view(), name='add_photo'),
    url(r'^album/add/$', views.AlbumFormView.as_view(), name='add_album'),
    url(r'^photo/(?P<pk>\d+)/edit/$', views.PhotoFormView.as_view(), name='edit_photo'),
    url(r'^album/(?P<pk>\d+)/edit/$', views.AlbumFormView.as_view(), name='edit_album'),
]
