from django.db import models
from base.base_model import BaseModel
from posts.models import Post
from comments.models import Comment

class Media(BaseModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True, blank=True)
    file_name = models.CharField(max_length=255)
    file_path = models.CharField(max_length=255)
    file_type = models.CharField(max_length=50, blank=True, null=True)


    def __str__(self):
        return self.file_name