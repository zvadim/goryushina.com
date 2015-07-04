from django.conf.urls import url, patterns

from apps.redactor.views import RedactorUploadView
from apps.redactor.forms import FileForm, ImageForm


urlpatterns = patterns(
    '',
    url(r'^upload/image/(?P<upload_to>.*)',
        RedactorUploadView.as_view(form_class=ImageForm),
        name='redactor_upload_image'),

    url(r'^upload/file/(?P<upload_to>.*)',
        RedactorUploadView.as_view(form_class=FileForm),
        name='redactor_upload_file'),
)
