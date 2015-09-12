from django.contrib import admin
from polymorphic.admin import PolymorphicChildModelAdmin
from .models import Category


@admin.register(Category)
class CategoryAdmin(PolymorphicChildModelAdmin):
    base_model = Category
    prepopulated_fields = {'slug': ('title',)}
