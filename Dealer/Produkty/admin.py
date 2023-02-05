from django.contrib import admin
from .models import Producent, Rodzaj, Produkty
# Register your models here.

admin.site.register(Producent)
admin.site.register(Produkty)
admin.site.register(Rodzaj)
