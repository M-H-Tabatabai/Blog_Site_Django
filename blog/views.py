from django.shortcuts import render, get_object_or_404
from blog.models import Post


def blog(request):
    posts = Post.objects.filter(status = True)
    context = {"posts": posts} 
    return render(request, "blog/blog-home.html", context)

def single_blog(request):
    return render(request, "blog/blog-single.html")

def test(request):
    posts = Post.objects.all()
    context = {"post_1": posts, "name":["hossein", "ali", "abbas"]} 
    return render(request, "test.html", context)

def test2(request, pid):
    post = get_object_or_404(Post, id=pid)
    return render(request, "test.html", {"posts": post})

