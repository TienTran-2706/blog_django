from django.db import models
from django.contrib.auth.models import User
from base.base_model import BaseModel
from base.slug_mixin import SlugMixin

class Post(BaseModel, SlugMixin):

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
    featured_image = models.ImageField(upload_to='media', blank=True)
    thumbnail = models.ImageField(upload_to='media', blank=True)
    published_at = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    def __str__(self):
        return self.title
