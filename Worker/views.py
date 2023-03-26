from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.http import HttpResponse



def home(request):
    return render(request, 'Worker/login.html')
