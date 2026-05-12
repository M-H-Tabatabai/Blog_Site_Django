from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse

def Home(request):
    return HttpResponse("<h1>hello world!<h1>")

def About_Me(request):
    return JsonResponse({"name": "mohammad-hossein", "last_name" : "tabatabai", "age" : "25"})

def Contact(request):
    return HttpResponse("contact")
