from django.db import models
from polymorphic import PolymorphicModel


class Menu(models.Model):
    title = models.CharField(max_length=64)
    order = models.IntegerField(default=999, editable=False)
    linked_object = models.ForeignKey('menu.MenuItem')
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ('order',)

    def __str__(self):
        return self.title


class MenuItem(PolymorphicModel):
    pass

