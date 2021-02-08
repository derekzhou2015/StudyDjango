from django.shortcuts import render, HttpResponse, redirect


# Create your views here.


def list(request):
    return HttpResponse('Hello Book')
