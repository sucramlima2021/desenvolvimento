from django.db import models
from .clientes import *
from .angariadores import Angariadores
from .apolices_geral import *

class Decesso(ApoliceBase):
    taxa = models.FloatField( null=True, blank=True)
    observacoes = models.TextField( null=True, blank=True)
    angariador = models.ForeignKey(Angariadores, on_delete=models.PROTECT, null=True, blank=True)
    datacancelamento = models.DateField( null=True, blank=True)
    producao = models.DateField( null=True, blank=True)
    averbacao = models.DateField( null=True, blank=True)
    clube = models.CharField(max_length=255, null=True, blank=True)
    anuencia = models.BooleanField(default=False)  
    subconv = models.IntegerField( null=True, blank=True)  
    codunid = models.IntegerField( null=True, blank=True)  

    def __str__(self):
        base = super().__str__()
        return base