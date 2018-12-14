from polymorphic.admin import PolymorphicChildModelAdmin
from sorl.thumbnail.admin import AdminImageMixin

from django.contrib import admin

from apps.changelist_ordering.admin import ChangeListOrdering
from apps.gallery.models import Image

from .models import Page, Category


class GalleryInline(AdminImageMixin, admin.StackedInline):
    model = Image


class PageAdmin(AdminImageMixin, PolymorphicChildModelAdmin, ChangeListOrdering):
    base_model = Page
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'group', 'is_active', 'create_date')
    list_filter = ('group', 'is_active')
    list_display_links = ('title',)
    inlines = (GalleryInline,)


class CategoryAdmin(PolymorphicChildModelAdmin):
    base_model = Category
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Page, PageAdmin)
admin.site.register(Category, CategoryAdmin)
