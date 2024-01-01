from django.http import HttpResponseForbidden
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import *
from .forms import *
from django.contrib import messages


@login_required
def create_blog_post(request):
    # Prevent users to create new blog posts
    if not request.user.user_role == 'blogger':
        return HttpResponseForbidden('You do not have permission to create blog')
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user
            blog_post.save()
            messages.success(request, 'Blog post created successfully')
            return redirect('view_profile')
    else:
        form = BlogPostForm()
    return render(request, 'create_blog_post.html', {'form': form})


@login_required
def get_all_blogs(request):
    blogs = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'blog_list.html', {'blogs':blogs})

@login_required
def blog_detail(request, slug):
    blog = get_object_or_404(BlogPost, slug=slug)
    return render(request, 'blog_detail.html', {'blog': blog})



@login_required
def update_blog_post(request, slug):
    # Ensure the user has the permission to update the blog post
    if not request.user.user_role == 'blogger':
        return HttpResponseForbidden('You do not have permission to update blog')

    blog_post = get_object_or_404(BlogPost, slug=slug, author=request.user)

    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=blog_post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Blog post updated successfully')
            return redirect('view_profile')
    else:
        form = BlogPostForm(instance=blog_post)

    return render(request, 'update_blog_post.html', {'form': form, 'blog_post': blog_post})


#delete blog post
@login_required
def delete_blog_post(request, id):
    blog_post = get_object_or_404(BlogPost, id=id)
    if not (request.user.user_role == 'blogger' and blog_post.author == request.user):
        return HttpResponseForbidden('You do not have permission to delete this blog post.')
    
    if request.method == 'POST':
        blog_post.delete()
        messages.success(request, 'Blog post deleted successfully.')
        return redirect('view_profile')
    
    return render(request, 'delete_blog.html', {'blog_post': blog_post})


# Search features using Q lookup
@login_required
def search_blogs(request):
    query = request.GET.get('q', '')
    if query:
       blogs = BlogPost.objects.filter(Q(title__contains=query) | Q(content__contains=query))
    else:
        blogs = BlogPost.objects.all()

    return render(request, 'blog_search_results.html', {'blogs':blogs, 'query': query})


