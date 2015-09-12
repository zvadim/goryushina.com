import importlib
from django.core.urlresolvers import resolve
from django.views.generic import View, DetailView
from apps.page.models import Page, Category
from apps.menu.models import Menu


class MainPageView(View):
    def dispatch(self, request, *args, **kwargs):
        # The first menu is also the main page
        first_menu_item = Menu.objects.first()

        view_func = resolve(first_menu_item.get_url()).func
        module = importlib.import_module(view_func.__module__)
        view = getattr(module, view_func.__name__)

        kwargs['slug'] = first_menu_item.linked_object.get_real_instance().slug
        return view.as_view()(request, *args, **kwargs)


class PageView(DetailView):
    template_name = 'page.html'
    model = Page


class CategoryView(DetailView):
    template_name = 'category.html'
    model = Category


# handlers
main_page_handler = MainPageView.as_view()
page_handler = PageView.as_view()
category_handler = CategoryView.as_view()
