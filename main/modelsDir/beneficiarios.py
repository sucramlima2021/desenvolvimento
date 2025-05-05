from django.db import models
from .clientes import *
from .apolices_geral import *
class Beneficiarios(models.Model):
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    apolice = models.ForeignKey(ApolicesGerais, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50, null=True, blank=True)
    nascimento = models.DateTimeField(null=True, blank=True)
    cpf = models.CharField(max_length=11, null=True, blank=True)
    parentesco = models.CharField(max_length=30, null=True, blank=True)
    percentual = models.FloatField(null=True, blank=True)
    controle = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return str(self.apolice)
