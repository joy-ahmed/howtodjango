from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'author',)