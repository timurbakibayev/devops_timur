from django.contrib import admin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import path


def hello(request: HttpRequest) -> HttpResponse:
    return render(request, "index.html")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hello),
]
