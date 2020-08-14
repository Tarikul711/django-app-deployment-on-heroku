from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('showall/', views.showall),
    path('update/', views.update),
    path('delete/', views.delete),
]
