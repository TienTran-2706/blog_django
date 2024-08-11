from django.contrib import admin
from .models import Category
from django.contrib.admin import ModelAdmin

@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ('name','slug','created_at','updated_at')
    search_fields = ('name', 'slug')

