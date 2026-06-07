from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect

def login_view(request):
    if request.user.is_authenticated:
        return redirect('/website/')

    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/website/')

    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    return render(request, "accounts/logout.html")

def signup_view(request):
    return render(request, "accounts/signup.html")