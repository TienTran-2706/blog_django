from django.db import models
from django.utils.text import slugify

class SlugMixin(models.Model):
    slug = models.SlugField(unique=True, max_length=255)

    class Meta:
        abstract = True

    #Auto create slug from title
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            # Ensure slug uniqueness
            num = 1
            while self.__class__.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{num}"
                num += 1
            self.slug = slug
        super().save(*args, **kwargs)
