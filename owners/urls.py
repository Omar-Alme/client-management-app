from django.urls import path
from . import views


urlPatterns = [
  path('owners/', views.profile, name='profile'),

]