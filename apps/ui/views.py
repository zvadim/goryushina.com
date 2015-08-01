from django.views.generic import TemplateView, DetailView, ListView
from apps.page.models import Page


class MainPageView(TemplateView):
    template_name = 'base.html'


class PageView(DetailView):
    model = Page


class CategoryView(ListView):
    pass


# handlers
main_page_handler = MainPageView.as_view()
page_handler = PageView.as_view()
category_handler = CategoryView.as_view()
