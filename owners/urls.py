from django.urls import path
from . import views


urlpatterns = [
  path('owners/', views.profile, name='profile'),
  path('save_profile/', views.save_profile, name='save_profile'),
]