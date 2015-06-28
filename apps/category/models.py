from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    slug = models.SlugField()

    class Meta:
        ordering = ('title',)

    def __unicode__(self):
        return self.title
