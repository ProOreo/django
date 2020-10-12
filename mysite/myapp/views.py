from django.shortcuts import render
from django.http import HttpResponse

# myapp/views.py
from django.http import HttpResponse


def homepage_view(request):
    return HttpResponse('Django says: Hello World!')
