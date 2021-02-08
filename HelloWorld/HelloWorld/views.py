from django.http import HttpResponse
from django.shortcuts import render, redirect


def index(request):
    context = {'title': 'Welcome to Hello World'}
    return render(request, 'index.html', context)


def hello(request):
    ls = [chr(item) for item in range(65, 91)]
    return render(request, 'hello.html', {"context": ls})


def show(request):
    context = {'name': 'kerwin', 'age': 24, 'gender': 'male'}
    return render(request, 'show.html', context)
