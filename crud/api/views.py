from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponse, JsonResponse
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.db import IntegrityError
from django.contrib import messages
from django.contrib.auth.password_validation import validate_password
from crud.settings import PASSWORD_SALT
from .utils import make_hash_with_salt, user_data_in_dict
from .models import User


def create(request):
    if request.method == "POST":
        psw = request.POST["password"]
        try:
            validate_password(psw)
            password_hash_with_salt = make_hash_with_salt(PASSWORD_SALT, psw)
            user_obj = User(username=request.POST["username"], password=password_hash_with_salt)
            user_obj.save()
        except ValidationError as psw_validation_exc:
            print(psw_validation_exc)
            return JsonResponse({"msg" : f"{str(psw_validation_exc)}"}, status=400)
        except IntegrityError as not_unique_username_exc:
            return JsonResponse({"msg" : f"User with username '{user_obj.username}' already exists."}, status=400)
        except Exception as exc:
            print("----- Error -----\n" + str(exc) + "\n-----------------")
            return JsonResponse({"msg" : "Error while creating a new user."}, status=500)
        else:
            messages.success(request, f"Пользователь {user_obj.username} c ID={user_obj.id} был успешно создан!")
            return redirect(reverse("index"))
    else:
        return JsonResponse({"msg" : "HTTP-method must be 'POST' to interactive with this page."}, status=405)


def read(request):
    if request.method == "GET":
        user_id = request.GET["id"]
        if user_id == "" or user_id.isnumeric():

            if user_id == "":
                found_user = User.objects.all()
            else:
                try:
                    found_user = User.objects.get(id=user_id)
                except ObjectDoesNotExist:
                    return JsonResponse({"msg" : f"User with ID={user_id} does not exist."}, status=404)

            return JsonResponse(
                user_data_in_dict(found_user),
                status=200
            )

        else:
            return JsonResponse({"msg" : "Passed user's ID must be integer or empty string."}, status=404)
    else:
        return JsonResponse({"msg" : "HTTP-method must be 'GET' to interactive with this page."}, status=405)


def update(request):
    return HttpResponse("Изменяю...")


def delete(request):
    return HttpResponse("Удаляю...")