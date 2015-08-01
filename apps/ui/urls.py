from django.conf.urls import url, patterns

urlpatterns = patterns(
    'apps.ui.views',
    url(r'^page/(?P<slug>.+)/$', 'page_handler', name='page'),
    url(r'^category/(?P<slug>.+)/$', 'category_handler', name='category'),
    url(r'^$', 'main_page_handler', name='index'),
)
