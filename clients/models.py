from django.db import models
from owners.models import owner

# Create your models here.
class client(models.Model):
    business_owner = models.ForeignKey(owner, on_delete=models.CASCADE, blank=True, null=True)
    company_logo = models.ImageField(upload_to='profile_pics', blank=True)
    client_name = models.CharField(max_length=50, blank=True, null=True)
    industry = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=50, unique=True, blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True, null=True, default="No bio yet")
    online_presence = models.URLField(max_length=200, blank=True, null=True)

   
# class Task(models.Model):

#     PRIOTIRY_CHOICES = [
#         ('H', 'High'),
#         ('M', 'Medium'),
#         ('L', 'Low'),
#     ]

#     STATUS_CHOICES = [
#         ('completed', 'Completed'),
#         ('inprogress', 'In Progress'),
#         ('todo', 'To Do'),
#     ]

#     client = models.ForeignKey(client, on_delete=models.CASCADE)
#     task_name = models.CharField(max_length=250, blank=True, null=True)
#     priority = models.CharField(max_length=10, choices=PRIOTIRY_CHOICES, default='L', blank=True, null=True)
#     status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='todo', blank=True, null=True)
#     deadline = models.DateField(blank=True, null=True)
#     is_completed = models.BooleanField(default=False, blank=True, null=True)
