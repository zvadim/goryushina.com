from django.contrib import admin
from changelist_ordering.admin import ChangeListOrdering
from .models import Menu


@admin.register(Menu)
class MenuAdmin(ChangeListOrdering):
    list_display = ('title', 'linked_object')
    list_display_links = ('title',)
    ordering = ('order',)


