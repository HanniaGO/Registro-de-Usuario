# users/views.py

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm

def index(request):
    return HttpResponse("<h1>Hello, world.</h1>")

def inicio(request):
    context = {
        "name": "Hannia GO",
        "message": "Por donde comenzamos.",
        "age": 21,
        "example_list": [22, 0, 9, 2, 2, 4]
    }
    return render(request, "base.html", context=context)

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('inicio')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})