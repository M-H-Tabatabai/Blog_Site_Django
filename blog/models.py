from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    # author
    # image
    title = models.CharField(max_length=255)
    content = models.TextField()
    # category
    # tag
    counted_view = models.IntegerField(default= 0)
    status = models.BooleanField(null=True)
    published_date = models.DateTimeField(default = timezone.now)
    created_date = models.DateTimeField(auto_now_add= True)
    updated_date = models.DateTimeField(auto_now= True)

    def __str__(self):
        return f"title : {self.title} - id : {self.id}"
