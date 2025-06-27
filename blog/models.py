from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.core.exceptions import ValidationError

USER = get_user_model()

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(USER, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publish = models.BooleanField(default=True)

    def __str__(self):
        return self.title


    
    
   
    