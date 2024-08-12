from django.db import models

class BaseExcerptModel(models.Model):
    excerpt = models.TextField(blank=True, null=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        # Auto generate excerpt for post base on content if excerpt is not provided by user
        if not self.excerpt and hasattr(self, 'content'):
            self.excerpt = self.generate_excerpt()
        super().save(*args, **kwargs)

    def generate_excerpt(self):
        #Generate excerpt from content (first 100 characters)
        content = getattr(self, 'content', '')
        return content[:100] + '...' if len(content) > 100 else content
