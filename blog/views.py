from django.shortcuts import render, get_object_or_404
from blog.models import Post


def blog(request):
    posts = Post.objects.filter(status = True)
    context = {"posts": posts} 
    return render(request, "blog/blog-home.html", context)

def single_blog(request, pid):
    posts = Post.objects.filter(status = True)
    post = get_object_or_404(posts, id=pid)
    context = {"post":post}
    return render(request, "blog/blog-single.html", context)

def test(request):
    posts = Post.objects.all()
    context = {"posts": posts, "name":["hossein", "ali", "abbas"]} 
    return render(request, "test.html", context)

def test2(request, pid):
    post = get_object_or_404(Post, id=pid)
    return render(request, "test.html", {"posts": post})

