from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Post
# Register your models here.

@admin.register(Post)
class PostAdmin(ModelAdmin):
    list_display = ('thumbnail_image','title','category','user')
    search_fields = ('title', 'category', 'user')

    def thumbnail_image(self, obj):
            if obj.thumbnail:
                return '<img src="%s" width="100" height="100"/>' % obj.thumbnail.url
            return 'No Image'

    thumbnail_image.short_description = 'Thumbnail'
