from django import template

register = template.Library()

@register.simple_tag(takes_context=True, name= "request_MU")
def counter (context):
    request = context.get("request")
    return f"method : {request.method} \\ user : {request.user}"

