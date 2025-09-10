from django.db import models
from .clientes import *
from .apolices_geral import *
from .beneficiarios import *
from .angariadores import *
from simple_history.models import HistoricalRecords

class ApolicesM(ApoliceBase):
    isbasica = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    diagnostico = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    auxbaba = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    observacoes = models.TextField(null=True, blank=True)
    taxa = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True)
    datacancelamento = models.DateField(null=True, blank=True)
    averbacao = models.DateField(null=True, blank=True)
    producao = models.DateField(null=True, blank=True) 
    angariador = models.ForeignKey(Angariadores, on_delete=models.PROTECT, null=True, blank=True)
    nome = models.CharField(max_length=50, null=True, blank=True)
    nascimento = models.DateField(null=True, blank=True)
    cpf = models.CharField(max_length=20, null=True, blank=True)
    clube = models.CharField(max_length=50, null=True, blank=True)
    tabela = models.CharField(max_length=50, null=True, blank=True)
    coluna = models.IntegerField(null=True, blank=True)
    anuencia = models.BooleanField()
    subconv = models.IntegerField(null=True, blank=True)
    codunid = models.IntegerField(null=True, blank=True)
    beneficiario1 = models.TextField(null=True, blank=True)
    beneficiario2 = models.TextField(null=True, blank=True)
    beneficiario3 = models.TextField(null=True, blank=True)
    history = HistoricalRecords()
    #beneficiariosNovos = models.ManyToManyField(BeneficiariosNovos, through="MulherBeneficiario", related_name="ApolicesM", blank=True)
    
    def __str__(self):
        base = super().__str__()
        return base
