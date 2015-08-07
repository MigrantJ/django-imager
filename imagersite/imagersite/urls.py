from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin
from imager_images import views


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^imager/', include('imager_images.urls')),
    url(r'^profile/', include('imager_profile.urls')),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/v1/', include('imager_api.urls'))
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
