from django.shortcuts import render
from django.http import  HttpResponse
from .models import Produkty
from .models import Producent


# Create your views here.

def index(request):
    zapytanie = Produkty.objects.all()
    # zapytanie = Sprzedaz.objects.all()
    return HttpResponse(zapytanie)
