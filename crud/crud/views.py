from django.shortcuts import render


def index(request):
    return render(request, "index.html")

def create_form_view(request):
    return render(request, "create_form.html")

def read_form_view(request):
    return render(request, "read_form.html")

def update_form_view(request):
    return render(request, "update_form.html")

def delete_form_view(request):
    return render(request, "delete_form.html")