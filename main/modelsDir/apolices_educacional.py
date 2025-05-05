from django.db import models
from .clientes import *
from .apolices_geral import *


class ApolicesE(models.Model):
    apolice = models.ForeignKey(ApolicesGerais, on_delete=models.CASCADE)
    matricula = models.IntegerField(null=True, blank=True)
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    movimento = models.CharField(max_length=1, null=True, blank=True)
    premio = models.FloatField(null=True, blank=True)
    isbasica = models.FloatField(null=True, blank=True)
    observacoes = models.TextField(null=True, blank=True)
    beneficiarios = models.TextField(null=True, blank=True)
    ultimoreajuste = models.DateTimeField(null=True, blank=True)
    penultimoreajuste = models.DateTimeField(null=True, blank=True)
    premioanterior = models.FloatField(null=True, blank=True)
    vigencia = models.DateTimeField(null=True, blank=True)
    taxa = models.FloatField(null=True, blank=True)
    datacancelamento = models.DateTimeField(null=True, blank=True)
    averbacao = models.DateTimeField(null=True, blank=True)
    producao = models.DateTimeField(null=True, blank=True)
    inicio = models.DateTimeField(null=True, blank=True)
    angariador = models.CharField(max_length=50, null=True, blank=True)
    controle = models.CharField(max_length=15, null=True, blank=True)
    certificado = models.BooleanField()
    clube = models.CharField(max_length=50, null=True, blank=True)
    idade = models.IntegerField(null=True, blank=True)
    nascimento = models.DateTimeField(null=True, blank=True)
    alterado = models.BooleanField()
    tabela = models.CharField(max_length=50, null=True, blank=True)
    coluna = models.IntegerField(null=True, blank=True)
    anuencia = models.BooleanField()
    subconv = models.IntegerField(null=True, blank=True)
    tipo = models.CharField(max_length=10, null=True, blank=True)
    premioant = models.FloatField(null=True, blank=True)
    isant = models.FloatField(null=True, blank=True)
    
    def __str__(self):
        return str(self.matricula)

class HistoricoE(models.Model):
    apolice = models.ForeignKey(ApolicesE, on_delete=models.CASCADE)
    alteracao = models.CharField(max_length=255)
    valoratual = models.CharField(max_length=255)
    valorantigo = models.CharField(max_length=255)
    observacoes = models.TextField()
    
    def __str__(self):
        return f'{self.alteracao} - Atual {self.valoratual} - Anterior {self.valorantigo}'