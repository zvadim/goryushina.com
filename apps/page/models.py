from django.db import models
from apps.redactor.fields import RedactorField
from apps.menu.models import MenuItem


class Page(MenuItem):
    title = models.CharField(max_length=128)
    text = RedactorField(
        verbose_name=u'Text',
        allow_file_upload=False,
        allow_image_upload=True
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
        # FIXME:
        return self.slug

    def __unicode__(self):
        return '%s: %s' % (self.object_type(), self.title)
