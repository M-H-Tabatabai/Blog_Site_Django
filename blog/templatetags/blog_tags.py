from django import template
from blog.models import Post
from blog.models import Category

register = template.Library()

@register.simple_tag(takes_context=True, name= "request_MU")
def counter (context):
    request = context.get("request")
    return f"method : {request.method} \\ user : {request.user}"

@register.simple_tag(name= "latest")
def latest_post():
    posts = Post.objects.all()[:2]
    post_list = []
    for post in posts:
        post_list.append(post.title)
    return f"post list = {post_list}"

@register.simple_tag(name="latest2")
def latest_post2(posts):
    post_list = []
    for post in posts:
        post_list.append(post.title)
    return post_list[:2]

@register.filter(name = "slicer")
def end_slicer(text):
    return text[:5] + "..."

@register.inclusion_tag("test_popularposts.html")
def popularposts():
    posts = Post.objects.filter(status = True)
    return {"posts": posts}

@register.inclusion_tag("blog/latest-post.html")
def latest_post():
    posts = Post.objects.filter(status = True)[:3]
    context = {"posts":posts}
    return context

@register.inclusion_tag("blog/blog-category.html")
def category_list():
    posts = Post.objects.filter(status = True)
    categories = Category.objects.all()
    category_dict = {}
    for name in categories:
        category_dict[name] = posts.filter(category=name).count()
    sorted_dict = dict(sorted(category_dict.items(), key=lambda item: item[1], reverse=True))
    return {'category_dict': sorted_dict}
