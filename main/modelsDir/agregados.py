from django.db import models
from .clientes import *
class Agregados(models.Model):
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50, null=True, blank=True)
    nascimento = models.DateTimeField(null=True, blank=True)
    idade = models.IntegerField(null=True, blank=True)
    parentesco = models.CharField(max_length=50, null=True, blank=True)
    cpf = models.CharField(max_length=50, null=True, blank=True)
    valor = models.FloatField(null=True, blank=True)
    nivel = models.IntegerField(null=True, blank=True)
    angariador = models.ForeignKey(Angariadores, on_delete=models.PROTECT, null=True, blank=True)
    clube = models.CharField(max_length=50, null=True, blank=True)
    observacoes = models.TextField(null=True, blank=True)
    vigencia = models.DateTimeField(null=True, blank=True)
    subconv = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return str(f'{self.cliente} - {self.nome} - {self.parentesco}')