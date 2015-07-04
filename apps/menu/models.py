from django.db import models

class Menu(models.Model):
    title = models.CharField(max_length=64)
    order = models.IntegerField(default=999, editable=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ('order',)

    def __str__(self):
        return self.title


