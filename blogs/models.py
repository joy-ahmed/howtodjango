from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

from blog_users.models import CustomUser

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(blank=True)
    cover_image = models.ImageField(upload_to="blog/images/", blank=True, null=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = RichTextField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    