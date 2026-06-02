from django.shortcuts import render, get_object_or_404
from blog.models import Post,Comment
from django.core.paginator import Paginator
from taggit.models import Tag
from django.db.models import Count,Q

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


def blog(request, cat_name=None, author_name=None, tag_name=None):
    posts = Post.objects.filter(status=True).annotate(
        comments_count=Count(
            "comment",
            filter=Q(comment__approved=True)
        )
    ).order_by("-created_date")
    if author_name:
        posts = posts.filter(author__username=author_name)
    if cat_name:
        posts = posts.filter(category__name=cat_name)
    if tag_name:
        posts = posts.filter(tags__name=tag_name)

    paginator = Paginator(posts, 3)
    page_number = request.GET.get("page")
    posts = paginator.get_page(page_number)

    common_tags = Tag.objects.annotate(
        num_times=Count("taggit_taggeditem_items")
    ).order_by("-num_times")[:10]
    

    context = {"posts": posts, "common_tags": common_tags, "active_tag": tag_name}
    return render(request, "blog/blog-home.html", context)


def single_blog(request, pid):
    posts = Post.objects.filter(status=True)
    post = get_object_or_404(posts, id=pid)
    comments = Comment.objects.filter(approved=True, post=post.id)
    common_tags = Tag.objects.annotate(
        num_times=Count("taggit_taggeditem_items")
    ).order_by("-num_times")
    context = {"post": post, "common_tags": common_tags, "comments" : comments}
    return render(request, "blog/blog-single.html", context)


def category_blog(request, cat_name):
    posts = Post.objects.filter(status=True)
    posts = posts.filter(category__name=cat_name)
    context = {"posts": posts}
    return render(request, "blog/blog-home.html", context)


def search_blog(request):
    posts = Post.objects.filter(status=True)
    query = request.GET.get("q")
    if query:
        posts = posts.filter(content__icontains=query)
    context = {"posts": posts}
    return render(request, "blog/blog-home.html", context)


def test(request):
    posts = Post.objects.all()
    context = {"posts": posts, "name": ["hossein", "ali", "abbas"]}
    return render(request, "test.html", context)


def test2(request, pid):
    post = get_object_or_404(Post, id=pid)
    return render(request, "test.html", {"posts": post})
