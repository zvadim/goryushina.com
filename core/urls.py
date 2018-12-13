from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from filebrowser.sites import site

urlpatterns = [
    url(r'^admin/filebrowser/', site.urls),
    url(r'^admin/', admin.site.urls),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^', include('apps.ui.urls', namespace='ui')),
]

# For development only
if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
