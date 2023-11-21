from django.urls import path
from . import views


urlpatterns = [
  path('owners/', views.profile, name='profile'),
  path('owners/', views.edit_profile, name='edit_profile'),
]