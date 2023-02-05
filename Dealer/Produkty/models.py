from django.db import models

# Create your models here.

class Producent(models.Model):
    def __str__(self):
        return self.nazwa
    nazwa = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Auto'
        verbose_name_plural = 'Producent'
        
class Rodzaj(models.Model):
    def __str__(self):
        return self.nazwa
    nazwa = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Auto'
        verbose_name_plural = 'Rodzaj'

class Produkty(models.Model):
    Rodzaj = models.ForeignKey(Rodzaj, null=True, blank=True,on_delete=models.CASCADE)
    producent = models.ForeignKey(Producent, on_delete=models.CASCADE,null=True)
    nazwa = models.CharField(max_length=100)
    rocznik = models.DecimalField(max_digits=12, decimal_places=2)
    opis = models.TextField(blank=True)
    cena = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        verbose_name = 'Auto'
        verbose_name_plural = 'Oferty sprzedaży'

    def __str__(self):
        return self.nazwa
