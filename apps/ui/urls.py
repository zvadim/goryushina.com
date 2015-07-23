from django.conf.urls import url, patterns

urlpatterns = patterns(
    'apps.ui.views',
    url(r'^$', 'main_page', name='index'),
)
