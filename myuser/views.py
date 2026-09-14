from django.shortcuts import render
from django.http import HttpResponse

def login(request):
    return HttpResponse("<h1>Login Page</h1>")

def signup(request):
    return HttpResponse("<h1>Signup Page</h1>")

def logout(request):
    return HttpResponse("<h1>logout Page</h1>")
