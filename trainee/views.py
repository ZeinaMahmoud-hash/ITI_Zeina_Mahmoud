from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Trainee

def alltrainee(request):
    context={'trainee':Trainee.objects.all()}
    return render(request, 'trainee/trainee.html', context=context)

def gettrainee(request, id):
    return HttpResponse(f"<h1>Trainee Details for ID: {id}</h1>")

def inserttrainee(request):
    if request.method =='POST':
        name=request.POST['trname']
        email=request.POST['tremail']
        image=request.FILES.get('trimage')
        Trainee.objects.create(name=name,email=email,image=image)
        return HttpResponse("<h1>inserted successfully</h1>")
    return render(request, 'trainee/insert.html')

def updatetrainee(request,id):
    trainee = Trainee.objects.get(id=id)
    if request.method =='POST':
        name = request.POST.get('trname')
        email = request.POST.get('tremail')
        image = request.FILES.get('trimage')
        trainee.name = name
        trainee.email = email
        if image:
            trainee.image = image
        trainee.save()
        return redirect('/trainee/')
    return render(request, 'trainee/updatetrainee.html', context={'trainee': trainee})


def deletetrainee(request,id):
    Trainee.objects.filter(id=id).update(status=False)
    return redirect('/trainee/')