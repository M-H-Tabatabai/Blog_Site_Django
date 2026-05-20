from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.core.paginator import Paginator

# another model used kwargs
# def blog(request, **kwargs):
#     posts = Post.objects.filter(status=True)

#     author_name = kwargs.get("author_name")
#     if author_name:
#         posts = posts.filter(author__username=author_name)

#     cat_name = kwargs.get("cat_name")
#     if cat_name:
#         posts = posts.filter(category__name=cat_name)

#     context = {"posts": posts}
#     return render(request, "blog/blog-home.html", context)

def blog(request, cat_name=None, author_name=None):
    posts = Post.objects.filter(status = True)
    if author_name:
        posts= posts.filter(author__username = author_name)
    if cat_name:
        posts = posts.filter(category__name = cat_name)

    paginator = Paginator(posts, 2)
    page_number = request.GET.get("page")
    posts = paginator.get_page(page_number)

    context = {"posts" : posts} 
    return render(request, "blog/blog-home.html", context)

def single_blog(request, pid):
    posts = Post.objects.filter(status = True)
    post = get_object_or_404(posts, id=pid)
    context = {"post":post}
    return render(request, "blog/blog-single.html", context)

def category_blog(request, cat_name):
    posts = Post.objects.filter(status = True)
    posts = posts.filter(category__name = cat_name)
    context = {"posts": posts}
    return render(request, "blog/blog-home.html", context)

def search_blog(request):
    posts = Post.objects.filter(status = True)
    query = request.GET.get("q")
    if query:
        posts = posts.filter(content__icontains = query)
    context = {"posts" : posts}
    return render(request, "blog/blog-home.html", context)

def test(request):
    posts = Post.objects.all()
    context = {"posts": posts, "name":["hossein", "ali", "abbas"]} 
    return render(request, "test.html", context)

def test2(request, pid):
    post = get_object_or_404(Post, id=pid)
    return render(request, "test.html", {"posts": post})
