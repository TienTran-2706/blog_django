from django.db import models
from base.base_model import BaseModel
from base.slug_mixin import SlugMixin

class Category(BaseModel, SlugMixin):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    def __str__(self):
        return self.name