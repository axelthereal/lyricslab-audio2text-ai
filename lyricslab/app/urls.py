"""
URL configuration for lyricslab project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
App Urls
""" 
from django.urls import path
from .views import *

urlpatterns = [
    # custom
    path('', home_view, name="default_pages_view"),
    path('home', home_view, name="home_view"), 

    # api_routes
    path('appnode/v1.0.1/runtime/upload', upload_media, name="media_upload"),
]
