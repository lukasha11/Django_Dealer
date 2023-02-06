from .models import Producent, Rodzaj, Produkty
from rest_framework import serializers

class ProduktySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Produkty
        fields = ['Rodzaj','producent','nazwa','rocznik','opis','cena']

class RodzajSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rodzaj
        fields = ['nazwa']

class ProducentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Producent
        fields = ['nazwa']