from bs4 import BeautifulSoup
from sorl.thumbnail import get_thumbnail

from django import template
from django.conf import settings

register = template.Library()


@register.filter()
def thumbnail_images(text, geometry_string='800'):
    soup = BeautifulSoup(text, "html.parser")

    img_tag = soup.find_all('img')
    for tag in img_tag:
        src = tag['src']
        if src.startswith(settings.MEDIA_URL):
            src = src[len(settings.MEDIA_URL):]
            im = get_thumbnail(src, geometry_string)
            tag['src'] = im.url
            tag['width'] = '100%'
            tag['height'] = ''

    return soup
