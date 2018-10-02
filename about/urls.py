from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('web-team/', views.web_team),
    path('about/', views.about)
]
