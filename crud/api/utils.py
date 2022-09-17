import hashlib
from typing import Union
from .models import User
from django.db.models import QuerySet


def make_hash_with_salt(salt: str, password: str) -> str:
    """Добавляет соль к переданному паролю, а затем хэширует в sha256"""
    encoded_string = (salt + password).encode("utf-8")
    hash = hashlib.sha256(encoded_string).hexdigest()
    return hash


def user_data_in_dict(obj: Union[QuerySet, User]) -> dict:
    """Функция принимает либо объект с информацией об одном юзере, либо 
    объект QuerySet с информацией о всех юзерах, после чего переводит
    всю информацию в словарь (для дальнейшего преобразования в JSON)"""
    if type(obj) == User:
        dataset = {
            "id" : obj.id,
            "username" : obj.username,
            "created_at" : obj.created_at,
            "updated_at" : obj.updated_at
        }
    else:
        dataset = {}
        for user in obj:
            dataset[user.id] = {
                "id" : user.id,
                "username" : user.username,
                "created_at" : user.created_at,
                "updated_at" : user.updated_at
            }
    return dataset
