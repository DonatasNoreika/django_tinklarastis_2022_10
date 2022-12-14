from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Irasas(models.Model):
    autorius = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    pavadinimas = models.CharField("Pavadinimas", max_length=200)
    tekstas = HTMLField("Tekstas")
    data = models.DateTimeField("Data", auto_now_add=True)

    def komentaru_skaicius(self):
        komentarai = Komentaras.objects.filter(irasas=self.pk)
        return len(komentarai)

    class Meta:
        verbose_name = 'Irašas'
        verbose_name_plural = 'Irašai'
        ordering = ['data']

    def __str__(self):
        return f"{self.autorius} - {self.pavadinimas} ({self.data})"

class Komentaras(models.Model):
    irasas = models.ForeignKey('Irasas', on_delete=models.CASCADE, related_name="komentarai", null=True, blank=True)
    autorius = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    tekstas = models.TextField("Tekstas", max_length=5000)
    data = models.DateTimeField("Data", auto_now_add=True)

    class Meta:
        verbose_name = 'Komentaras'
        verbose_name_plural = 'Komentarai'

    def __str__(self):
        return f"{self.autorius} ({self.data})"
