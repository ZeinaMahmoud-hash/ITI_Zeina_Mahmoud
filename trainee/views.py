from django.shortcuts import render
from django.http import HttpResponse

def alltrainees(request):
    trainees =[[1,"Zeina"],[2,"Mahmoud"],[3,"Magdy"]]
    return render(request, 'trainee/list.html', context={'trainees':trainees})

def gettrainee(request, id):
    return HttpResponse(f"<h1>Trainee Details for ID: {id}</h1>")

def updatetrainee(request, id):
    return HttpResponse(f"<h1>Update Trainee ID: {id}</h1>")

def deletetrainee(request, id):
    return HttpResponse(f"<h1>Delete Trainee ID: {id}</h1>")
