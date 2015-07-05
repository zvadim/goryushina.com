from django.db import models
from sorl.thumbnail import ImageField


def get_path(instance, name):
    return 'gallery/page_%s/%s' % (instance.page_id, name)

class Image(models.Model):
    title = models.CharField(max_length=255)
    file = ImageField(upload_to=get_path, width_field='width', height_field='height')

    width = models.IntegerField(editable=False)
    height = models.IntegerField(editable=False)

    create_dt = models.DateTimeField(auto_now_add=True)
    edit_dt = models.DateTimeField(auto_now=True)

    page = models.ForeignKey('page.Page')
