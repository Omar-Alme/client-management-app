from django.db import models
from owners.models import Owner

class Client(models.Model):
    business_owner = models.ForeignKey(Owner, on_delete=models.CASCADE, blank=True, null=True)
    company_logo = models.ImageField(upload_to='profile_pics', blank=True)
    client_name = models.CharField(max_length=50, blank=True, null=True)
    industry = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=50, unique=True, blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True, null=True, default="No bio yet")
    online_presence = models.URLField(max_length=200, blank=True, null=True)

   