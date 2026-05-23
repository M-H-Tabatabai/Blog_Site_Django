from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect

from website.models import Contact

from django.contrib import messages

from website.forms import ContactFormSimple, ContactModelForm, ContactForm, NewsletterForm

def index(request):
    return render(request, "website/index.html")

def about(request):
    return render(request, "website/about.html")

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "The contact creation was a success.")
            return HttpResponseRedirect("#")
        messages.success(request, "Creating a contact was not a success.")
    else:
        return render(request, "website/contact.html")
    
def newsletter(request):
    if request.method == "POST":
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Email successfully registered.")
            return HttpResponseRedirect("#")
        messages.error(request, "The email was not registered!")
    else:
        return render(request, "website/index.html")


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
