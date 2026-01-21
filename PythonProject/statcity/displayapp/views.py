from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Helllo, World!")

# Create your views here.
