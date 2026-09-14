from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('login/', login),
    path('signup/', signup),
    path('logout/', logout),
]