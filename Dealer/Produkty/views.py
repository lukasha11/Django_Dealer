# from django.shortcuts import render
# from django.http import  HttpResponse

from .models import Producent, Produkty, Rodzaj
from rest_framework import viewsets
from .serializer import RodzajSerializer, ProducentSerializer, ProduktySerializer


class RodzajViewSet(viewsets.ModelViewSet):
    queryset = Rodzaj.objects.all()
    serializer_class = RodzajSerializer


class ProducentViewSet(viewsets.ModelViewSet):
    queryset = Producent.objects.all()
    serializer_class = ProducentSerializer


class ProduktyViewSet(viewsets.ModelViewSet):
    queryset = Produkty.objects.all()
    serializer_class = ProduktySerializer
