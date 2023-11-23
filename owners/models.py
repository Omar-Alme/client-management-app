from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Owner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    business_name = models.CharField(max_length=50, unique=True, blank=True, null=True)
    email = models.EmailField(max_length=50, unique=True, blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True, null=True, default="No bio yet")
    website = models.URLField(max_length=200, blank=True, null=True)

