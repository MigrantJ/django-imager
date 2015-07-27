from django.conf.urls import include, url
from imager_images import views

urlpatterns = [
    url(r'^home/$', views.index, name='index'),
    url(r'^accounts/', include('registration.backends.default.urls')),
]
