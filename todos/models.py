from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=100, null = True)
    content = models.CharField(max_length=1000, null=True, blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    start = models.CharField(max_length=100, null=True, blank=True)
    end = models.CharField(max_length=100, null=True, blank=True)
    
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    
    def __str__(self) -> str:
        return self.title