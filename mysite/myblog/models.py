from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Irasas(models.Model):
    autorius = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    pavadinimas = models.CharField("Pavadinimas", max_length=200)
    tekstas = models.TextField("Tekstas", max_length=5000)
    data = models.DateTimeField("Data", auto_now_add=True)


class Komentaras(models.Model):
    irasas = models.ForeignKey('Irasas', on_delete=models.CASCADE, related_name="komentarai")
    autorius = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    tekstas = models.TextField("Tekstas", max_length=5000)
    data = models.DateTimeField("Data", auto_now_add=True)
