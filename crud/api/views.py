from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from crud.settings import PASSWORD_SALT
from .utils import make_hash_with_salt
from .models import User


def create(request):
    if request.method == "POST":
        try:
            password_hash_with_salt = make_hash_with_salt(PASSWORD_SALT, request.POST["password"])
            user_obj = User(username=request.POST["username"], password=password_hash_with_salt)
            user_obj.save()
        except Exception as e:
            print("----- Error -----\n" + str(e) + "\n-----------------")
            return JsonResponse({
                "error_msg" : "Error while creating a new user.",
                "status" : 500
            })
        else:
            messages.success(request, f"Пользователь {user_obj.username} c ID={user_obj.id} был успешно создан!")
            return redirect(reverse("index"))
    else:
        return JsonResponse({
            "error_msg" : "HTTP-method must be 'POST' to interactive with this page.",
            "status" : 400
        })

def read(request):
    return HttpResponse("Просматриваю...")

def update(request):
    return HttpResponse("Изменяю...")

def delete(request):
    return HttpResponse("Удаляю...")