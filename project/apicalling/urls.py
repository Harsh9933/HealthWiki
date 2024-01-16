from django.contrib import admin
from django.urls import path
from apicalling import views

urlpatterns = [
    path('',views.Welcome,name="home"),
    path('user',views.User,name="user")
]
    