from django.shortcuts import render
from django.http import request


def index(request):
    return render(request, 'app/index.html')



def signup(request):
    return render(request, 'app/signup.html')



def login(request):
    return render(request, 'app/login.html')
