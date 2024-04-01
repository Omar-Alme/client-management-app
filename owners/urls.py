from django.urls import path
from . import views


urlpatterns = [
  path('owners/', views.owner_profile, name='owner_profile'),
  path('owner_profile/', views.owner_profile, name='owner_profile'),
  path('edit_profile/', views.edit_profile, name='edit_profile'),
  path('save_profile/', views.save_profile, name='save_profile'),
]
