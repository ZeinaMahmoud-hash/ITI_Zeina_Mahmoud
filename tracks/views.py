from django.shortcuts import render
from django.http import HttpResponse

def alltracks(request):
    tracks=[[1,"Odoo"],[2,"Python"],[3,"Django"]]
    return render(request, 'tracks/list.html', context={'tracks':tracks})

def gettrack(request):
    return HttpResponse("<h1>inside first track</h1>")

def updatetrack(request,id):
    return HttpResponse(f"<h1>inside update {id} track</h1>")

def deletetrack(request,id):
    return HttpResponse(f"<h1>inside delete {id} track</h1>")