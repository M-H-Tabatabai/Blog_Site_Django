from django.shortcuts import render

# Create your views here.
def loginview(request):
    return render(request, "accounts/login.html")

def logoutview(request):
    return render(request, "accounts/logout.html")

def signupview(request):
    return render(request, "accounts/signup.html")