from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse

from website.models import Contact

from website.forms import ContactFormSimple, ContactModelForm

def index(request):
    return render(request, "website/index.html")

def about(request):
    return render(request, "website/about.html")

def contact(request):
    return render(request, "website/contact.html")

def website_test(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        c = Contact()
        c.name = name
        c.email = email
        c.subject = subject
        c.message = message
        c.save()
    return render(request, "website/test.html")

def website_form(request):
    form = ContactModelForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()       
        else:
            form = ContactModelForm()

    return render(request, "website/test.html", {"form" : form})
