from django.db import models
from .clientes import *
from .apolices_geral import *
from simple_history.models import HistoricalRecords

class Sinistros(models.Model):
    SINISTRADO_CHOICES = [
        ('T', 'Titular'),  
        ('C', 'Conjuge'),
        ('O', 'Outro'),
        
    ]
    STATUS_CHOICES = [
        ('C', 'Comunicado'),  
        ('P', 'Pago'),
        ('R', 'Recusado'),
        
    ]
    cliente = models.ForeignKey(Clientes, on_delete=models.PROTECT)
    apolice = models.ForeignKey(ApoliceBase, on_delete=models.PROTECT)
    titular = models.CharField(max_length=1, choices = SINISTRADO_CHOICES, null=True, blank=True)
    premio = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    Is = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    iea_diag = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    ipa_aux = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    ifptd = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    valor = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    data = models.DateField(null=True, blank=True)
    tipo = models.CharField(max_length=50, null=True, blank=True)
    observacoes = models.TextField( null=True, blank=True)
    tipo_morte = models.CharField(max_length=100, null=True, blank=True)
    data_obito = models.DateField(null=True, blank=True)
    data_com_vg = models.DateField(null=True, blank=True)
    data_com_cia = models.DateField(null=True, blank=True)
    pago_recusa = models.BooleanField(default=True)
    data_recusa_pg = models.DateField(null=True, blank=True)
    nome_segurado = models.CharField(max_length=255, null=True, blank=True)
    cpf_segurado = models.CharField(max_length=50, null=True, blank=True)
    status = models.CharField(max_length=1, choices = STATUS_CHOICES, null=True, blank=True, default='C')
    history = HistoricalRecords()
    def __str__(self):
        return str(f'Sinistro - {self.cliente} - {self.apolice}')