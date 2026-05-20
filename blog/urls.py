"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from blog.views import *

app_name = "blog"

urlpatterns = [
    path("", blog, name="blog"),
    path("<int:pid>/", single_blog, name="single"),
    path("category/<str:cat_name>/", blog , name="category"),
    path("author/<str:author_name>", blog, name="author"),
    path("test/", test, name="test"),
    path("<int:pid>", test2, name="test2")
]
