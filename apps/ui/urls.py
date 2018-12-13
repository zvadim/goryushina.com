from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^page/(?P<slug>.+)/$', views.page_handler, name='page'),
    url(r'^category/(?P<slug>.+)/$', views.category_handler, name='category'),
    url(r'^$', views.main_page_handler, name='index'),
]
