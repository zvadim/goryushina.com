from django.db import models
from apps.menu.models import MenuItem


class Category(MenuItem):
    title = models.CharField(max_length=128)
    slug = models.SlugField()
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ('title',)

    def __unicode__(self):
        return 'Category: %s' % self.title
