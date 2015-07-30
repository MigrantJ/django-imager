from django.conf.urls import url
import views

urlpatterns = [
    url(r'^home/$', views.IndexView.as_view(), name='index'),
    url(r'^photo/add/$', views.PhotoFormView.as_view(), name='add_photo'),
    url(r'^album/add/$', views.AlbumFormView.as_view(), name='add_album'),
]
