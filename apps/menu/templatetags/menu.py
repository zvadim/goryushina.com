from django import template
from apps.menu.models import Menu

register = template.Library()


@register.inclusion_tag('menu/get_menu_tag.html', takes_context=True)
def get_menu(context):
    current_url = context['request']
    menu = list(Menu.objects.filter(is_active=True))
    for i, m in enumerate(menu):
        if i == 0 and current_url.path == '/':
            m.menu_active = True
        else:
            m.menu_active = True if m.get_url() == current_url.path else False

    return {
        'menu': menu
    }
