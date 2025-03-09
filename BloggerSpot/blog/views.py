from django.shortcuts import render, get_object_or_404
from .models import Post

def home(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/home.html', {'posts': posts})

def expanded_blog(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/expanded_blog.html', {'post': post})

def about(request):
    return render(request, 'blog/About.html')

def contact(request):
    return render(request, 'blog/Contact.html')
