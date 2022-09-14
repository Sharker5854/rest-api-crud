from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True, editable=False, verbose_name="User's ID")
    username = models.CharField(max_length=32, unique=True, verbose_name="Username")
    password = models.CharField(max_length=255, verbose_name="Password hash")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created account")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated account")