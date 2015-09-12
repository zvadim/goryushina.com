from polymorphic.admin import PolymorphicChildModelAdmin
from sorl.thumbnail.admin import AdminImageMixin
from mce_filebrowser.admin import MCEFilebrowserAdmin
from django.contrib import admin

from apps.gallery.models import Image
from apps.page.models import Category
from .models import Page


class GalleryInline(AdminImageMixin, admin.StackedInline):
    model = Image


@admin.register(Page)
class PageAdmin(PolymorphicChildModelAdmin, MCEFilebrowserAdmin):
    base_model = Page
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'category', 'is_active', 'create_date')
    list_filter = ('category', 'is_active')
    inlines = (GalleryInline,)


@admin.register(Category)
class CategoryAdmin(PolymorphicChildModelAdmin):
    base_model = Category
    prepopulated_fields = {'slug': ('title',)}