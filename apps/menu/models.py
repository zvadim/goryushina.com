from django.db import models
from polymorphic.models import PolymorphicModel


class Menu(models.Model):
    title = models.CharField(max_length=64)
    order = models.IntegerField(default=999, editable=False)
    linked_object = models.ForeignKey('menu.MenuItem')
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ('order',)

    def __str__(self):
        return self.title

    def get_url(self):
        return self.linked_object.get_real_instance().get_url()


class MenuItem(PolymorphicModel):
    def __str__(self):
        instance = self.get_real_instance()
        return '%s: %s' % (instance.object_type(), instance.title)
