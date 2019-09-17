from django.contrib import admin
from django.urls import path

from my_app import views

urlpatterns = [
    path('',views.home,name="home_page"),
]
