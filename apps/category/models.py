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

    @property
    def active_pages(self):
        return self.page_set.filter(is_active=True)

    def __str__(self):
        return '%s: %s' % (self.object_type(), self.title)

