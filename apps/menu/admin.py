from django.contrib import admin
from apps.changelist_ordering.admin import ChangeListOrdering
from .models import Menu, MenuItem


class MenuAdmin(ChangeListOrdering):
    list_display = ('title', 'linked_object')
    list_display_links = ('title',)
    ordering = ('order',)


admin.site.register(Menu, MenuAdmin)
admin.site.register(MenuItem)
