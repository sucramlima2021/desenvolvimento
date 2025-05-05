from django.db import models
from .clientes import *
class Decesso(models.Model):
    matricula = models.FloatField( null=True, blank=True)
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    premio = models.FloatField( null=True, blank=True)
    taxa = models.FloatField( null=True, blank=True)
    movimento = models.CharField(max_length=255, null=True, blank=True)
    observacoes = models.TextField( null=True, blank=True)
    controle = models.CharField(max_length=255, null=True, blank=True)
    angariador = models.CharField(max_length=255, null=True, blank=True)
    vigencia = models.DateTimeField( null=True, blank=True)
    inicio = models.DateTimeField( null=True, blank=True)
    datacancelamento = models.DateTimeField( null=True, blank=True)
    producao = models.DateTimeField( null=True, blank=True)
    averbacao = models.DateTimeField( null=True, blank=True)
    certificado = models.BooleanField()  # Tipo original: BIT
    clube = models.CharField(max_length=255, null=True, blank=True)
    idade = models.IntegerField( null=True, blank=True)  # Tipo original: SMALLINT
    nascimento = models.DateTimeField( null=True, blank=True)
    alterado = models.BooleanField()  # Tipo original: BIT
    premioanterior = models.FloatField( null=True, blank=True)
    anuencia = models.BooleanField()  # Tipo original: BIT
    subconv = models.IntegerField( null=True, blank=True)  # Tipo original: SMALLINT
    codunid = models.IntegerField( null=True, blank=True)  # Tipo original: SMALLINT
    tipo = models.CharField(max_length=255, null=True, blank=True)
    premioatn = models.FloatField( null=True, blank=True)
    isant = models.FloatField( null=True, blank=True)

    def __str__(self):
        return str(self.matricula)

class HistoricoDecesso(models.Model):
    apolice = models.ForeignKey(Decesso, on_delete=models.CASCADE)
    alteracao = models.CharField(max_length=255)
    valoratual = models.CharField(max_length=255)
    valorantigo = models.CharField(max_length=255)
    observacoes = models.TextField()
    
    def __str__(self):
        return f'{self.alteracao} - Atual {self.valoratual} - Anterior {self.valorantigo}'