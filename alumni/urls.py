from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('about.urls')),
    path('admin/', admin.site.urls),
    path('<str:username>/', include('accounts.urls')),
]
