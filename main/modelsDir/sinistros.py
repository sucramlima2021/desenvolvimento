from django.db import models
from .clientes import *
from .apolices_geral import *
class Sinistros(models.Model):
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    apolice = models.ForeignKey(ApolicesGerais, on_delete=models.CASCADE)
    titular = models.BooleanField( default=True)
    premio = models.FloatField( null=True, blank=True)
    Is = models.FloatField( null=True, blank=True)
    iea_diag = models.FloatField( null=True, blank=True)
    ipa_aux = models.FloatField( null=True, blank=True)
    ifptd = models.FloatField( null=True, blank=True)
    valor = models.FloatField( null=True, blank=True)
    data = models.DateField(null=True, blank=True)
    tipo = models.CharField(max_length=50, null=True, blank=True)
    observacoes = models.TextField( null=True, blank=True)
    tipo_morte = models.CharField(max_length=100, null=True, blank=True)
    data_obito = models.DateField(null=True, blank=True)
    data_com_vg = models.DateField(null=True, blank=True)
    data_com_cia = models.DateField(null=True, blank=True)
    pago_recusa = models.BooleanField( default=True)
    data_recusa_pg = models.DateField(null=True, blank=True)
    nome_segurado = models.CharField(max_length=255, null=True, blank=True)
    cpf_segurado = models.CharField(max_length=50, null=True, blank=True)
    controle = models.CharField(max_length=255, null=True, blank=True)
    
    

    def __str__(self):
        return str(f'Sinistro - {self.cliente} - {self.apolice}')

class HistoricoSinistros(models.Model):
    apolice = models.ForeignKey(Sinistros, on_delete=models.CASCADE)
    alteracao = models.CharField(max_length=255)
    valoratual = models.CharField(max_length=255)
    valorantigo = models.CharField(max_length=255)
    observacoes = models.TextField()
    
    def __str__(self):
        return f'{self.alteracao} - Atual {self.valoratual} - Anterior {self.valorantigo}'