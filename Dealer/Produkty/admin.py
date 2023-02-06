from django.contrib import admin
from .models import Producent, Rodzaj, Produkty
# Register your models here.


@admin.register(Produkty)
class IdeaProdukty(admin.ModelAdmin):
    list_display = ['Rodzaj', 'producent', 'cena']
    list_filter = ['Rodzaj', 'producent']


@admin.register(Producent)
class IdeaProducent(admin.ModelAdmin):
    list_display = ['nazwa']


@admin.register(Rodzaj)
class IdeaRodzaj(admin.ModelAdmin):
    list_display = ['nazwa']




