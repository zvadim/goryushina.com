from django.core.urlresolvers import reverse
from django.db import models
from apps.menu.models import MenuItem


class Category(MenuItem):
    title = models.CharField(max_length=128)
    slug = models.SlugField()
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ('title',)

    @staticmethod
    def object_type():
        return 'Category'

    def get_url(self):
        return reverse('ui:category', kwargs={'slug': self.slug})

    def __unicode__(self):
        return '%s: %s' % (self.object_type(), self.title)

