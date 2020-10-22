from django.contrib import admin
from django.urls import path, include
from library import views

urlpatterns = [
    path('', include('library.urls')),
    path('admin/', admin.site.urls, name="admin")
]
