from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def login_view(request):

    if request.user.is_authenticated:
        return HttpResponse(
            f"Welcome {request.user.username}. You are logged in."
        )

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('/website/')

        return render(
            request,
            'accounts/login.html',
            {
                'error': 'Username or Password is incorrect.'
            }
        )

    return render(request, 'accounts/login.html')

def logout_view(request):
    return render(request, "accounts/logout.html")

def signup_view(request):
    return render(request, "accounts/signup.html")