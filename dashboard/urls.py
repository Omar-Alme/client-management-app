from django.urls import path
from . import views

urlpatterns = [
  path('', views.dashboard, name='dashboard'),
  path('client_form/', views.client_form, name='client_form'),
]