from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', alltrainees),
    path('<int:id>/', gettrainee),
    path('update/<int:id>/', updatetrainee, name='updatetrainee'),
    path('delete/<int:id>/', deletetrainee, name='deletetrainee'),
]