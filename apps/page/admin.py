from django.contrib import admin

from apps.gallery.models import Image
from .models import Page

class GalleryInline(admin.StackedInline):
    model = Image

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'category', 'is_active', 'create_date')
    list_filter = ('category', 'is_active')
    inlines = (GalleryInline,)
