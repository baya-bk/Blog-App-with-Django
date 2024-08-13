from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1> And this is my cart</h1>')