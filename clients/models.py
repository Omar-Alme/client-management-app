from django.db import models
from owners.models import Owner
from django.contrib.auth.models import User

class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    client_name = models.CharField(max_length=50, blank=True, null=True)
    industry = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=50, unique=True, blank=True, null=True)
    bio = models.TextField(max_length=250, blank=True, null=True, default="No bio yet")
    online_presence = models.URLField(max_length=200, blank=True, null=True)

   