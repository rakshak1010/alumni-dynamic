from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('web-team/', views.web_team),
    path('about/', views.about),
    path('<str:username>/', include('accounts.urls')),
]
