from django.contrib import admin
from django.urls import path
from .views import LoginAPIView, RegisterApi
from .import views

urlpatterns = [
    path('register', RegisterApi.as_view()),
    path('sign_in', RegisterApi.as_view()),
    path('home-page', views.home_page, name='home-page'),
]
