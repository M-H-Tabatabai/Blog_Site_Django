from django import template
from blog.models import Post

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

