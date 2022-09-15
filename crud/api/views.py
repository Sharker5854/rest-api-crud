from django.shortcuts import render
from django.http import HttpResponse


def create(request):
    if request.method == "GET":
        return render(request, "api/create.html")

def read(request):
    return HttpResponse("Просматриваю...")

def update(request):
    return HttpResponse("Изменяю...")

def delete(request):
    return HttpResponse("Удаляю...")