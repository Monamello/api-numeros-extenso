from django.db import models
from .conversor import verifica_extenso

# Create your models here.

class Numero(models.Model):
    inteiro = models.IntegerField()
    extenso = models.CharField(max_length=256, null=True)