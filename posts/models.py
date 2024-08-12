from django.db import models
from django.contrib.auth.models import User
from base.base_model import BaseModel
from base.slug_mixin import SlugMixin
from base.base_excerpt import BaseExcerptModel

from media.models import Media
class Post(BaseModel, SlugMixin, BaseExcerptModel):

    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey('categories.Category', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, unique=True)
    content = models.TextField()
    #summary of the post content
    excerpt = models.TextField(blank=True, null=True)
    published_at = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    def __str__(self):
        return self.title

    def get_featured_image(self):
        media = Media.objects.filter(post=self, file_type='image', file_name__icontains='featured').first()
        return media.file_path if media else None

    def get_thumbnail(self):
        media = Media.objects.filter(post=self, file_type='image', file_name__icontains='thumbnail').first()
        return media.file_path if media else None
