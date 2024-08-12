from django.db import models
from base.base_model import BaseModel
from posts.models import Post
class Tag(BaseModel):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)


    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class PostTag(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('post', 'tag')
        verbose_name = 'Post Tag'
        verbose_name_plural = 'Post Tags'

    def __str__(self):
        return f'{self.post.title} - {self.tag.name}'