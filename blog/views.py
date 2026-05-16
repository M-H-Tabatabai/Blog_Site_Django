from django.shortcuts import render
from blog.models import Post


def blog(request):
    return render(request, "blog/blog-home.html")

def single_blog(request):
    return render(request, "blog/blog-single.html")

def test(request):
    posts = Post.objects.all()
    context = {"post_1": posts, "name":["hossein", "ali", "abbas"]} 
    return render(request, "test.html", context)

