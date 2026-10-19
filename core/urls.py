"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),

    # Rota para o aplicativo "cadastro"
    path('', include('cadastro.urls')),

    # Login e logout prontos do Django
    path('accounts/', include('django.contrib.auth.urls')),
]
