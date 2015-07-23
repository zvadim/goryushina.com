from django.views.generic import TemplateView


class MainPageView(TemplateView):
    template_name = 'base.html'


# handlers
main_page = MainPageView.as_view()
