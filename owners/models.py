from django.db import models
from django.contrib.auth.models import User



class Owner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    business_name = models.CharField(max_length=50, unique=True, blank=True, null=True)
    email = models.EmailField(max_length=50, unique=True, blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True, null=True, default="No bio yet")
    website = models.URLField(max_length=200, blank=True, null=True)

