from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    firstname = models.CharField(max_length=200,null=True)
    lastname = models.CharField(max_length=200,null=True)
    avatar = models.ImageField(upload_to="uploads/",null=True)
    date_of_birth = models.DateField(null=True)
    phone_number = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100, null=True)
    user =models.OneToOneField(User, on_delete=models.CASCADE,null=True, blank=True)
    
    
    