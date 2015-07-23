from django import template

register = template.Library()


@register.inclusion_tag('menu/get_menu_tag.html', takes_context=True)
def get_menu(context):
    current_url = context['request']

    return {
    }
