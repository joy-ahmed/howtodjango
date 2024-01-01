from django.urls import path
from .views import *

urlpatterns = [
    path('create-post/', create_blog_post, name="create-post"),
    path('all-post/', get_all_blogs, name="blogs"),
    path('search/', search_blogs, name='search_blogs'),
    path('<slug:slug>/', blog_detail, name='blog_detail'),
    path('update/<slug:slug>/', update_blog_post, name='update_blog_post'),
    path('delete/<int:id>/', delete_blog_post, name='delete_blog_post'),
]
