from django.db import models
from tinymce.models import HTMLField


class Page(models.Model):
    title = models.CharField(max_length=128)
    text = HTMLField(blank=True)
    slug = models.SlugField()

    category = models.ForeignKey('category.Category', blank=True, null=True)

    create_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ('title',)

    def __unicode__(self):
        return self.title
