from django.core.urlresolvers import reverse
from django.db import models
from tinymce.models import HTMLField

from apps.menu.models import MenuItem


class Page(MenuItem):
    title = models.CharField(max_length=128)
    text = HTMLField(
        verbose_name=u'Text',
        help_text='Best video/photo size is 695x390'
    )

    slug = models.SlugField()

    category = models.ForeignKey('category.Category', blank=True, null=True)

    create_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ('title',)
        
    @staticmethod
    def object_type():
        return 'Page'

    def get_url(self):
        return reverse('ui:page', kwargs={'slug': self.slug})

    def __str__(self):
        return '%s: %s' % (self.object_type(), self.title)
