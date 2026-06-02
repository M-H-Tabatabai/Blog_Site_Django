from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='blog/', default='blog/default.jpg')
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ManyToManyField(Category, related_name="posts")
    tags = TaggableManager()
    counted_view = models.IntegerField(default=0)
    status = models.BooleanField(null=True)
    published_date = models.DateTimeField(default=timezone.now)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_date"]

    def __str__(self):
        return f"title(obj) : {self.title}"
    
    def get_absolute_url(self):
        return reverse("blog:single",kwargs={'pid':self.id} )
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=254)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=254)
    message = models.TextField()
    approved = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_date"]

    def __str__(self):
        return f"title(obj) : {self.name}"

    
