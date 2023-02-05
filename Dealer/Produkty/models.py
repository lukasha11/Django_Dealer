from django.db import models

# Create your models here.

class Producent(models.Model):
    def str(self):
        return self.nazwa
    nazwa = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Auto'
        verbose_name_plural = 'Producent'
        
class Produkty(models.Model):
    nazwa = models.CharField(max_length=100)
    rocznik = models.DecimalField(max_digits=12, decimal_places=2)
    opis = models.TextField(blank=True)
    cena = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.nazwa
