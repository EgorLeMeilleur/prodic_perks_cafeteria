from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.http import HttpResponse



def home(request):
    return HttpResponse("<h4>ABOBA</h4>")
