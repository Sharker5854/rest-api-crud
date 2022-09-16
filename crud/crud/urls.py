"""crud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import delete_form_view, index, create_form_view, read_form_view, update_form_view, delete_form_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("create-form/", create_form_view, name="create_form"),
    path("read-form/", read_form_view, name="read_form"),
    path("update-form/", update_form_view, name="update_form"),
    path("delete-form/", delete_form_view, name="delete_form"),
    path("api/", include("api.urls"))
]
