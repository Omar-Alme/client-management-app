from django.urls import path
from . import views


urlpatterns = [
  path('owners/', views.profile, name='profile'),

]