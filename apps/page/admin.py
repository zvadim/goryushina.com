from polymorphic.admin import PolymorphicChildModelAdmin
from sorl.thumbnail.admin import AdminImageMixin
from django.contrib import admin

from apps.gallery.models import Image
from .models import Page


class GalleryInline(AdminImageMixin, admin.StackedInline):
    model = Image


@admin.register(Page)
class PageAdmin(PolymorphicChildModelAdmin):
    base_model = Page
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'category', 'is_active', 'create_date')
    list_filter = ('category', 'is_active')
    inlines = (GalleryInline,)
