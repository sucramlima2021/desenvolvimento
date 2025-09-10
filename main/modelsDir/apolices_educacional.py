from django.db import models
from .clientes import *
from .apolices_geral import *
from .beneficiarios import *
from .angariadores import *
from simple_history.models import HistoricalRecords

class ApolicesE(ApoliceBase):
    matricula = models.IntegerField(null=True, blank=True)
    isbasica = models.FloatField(null=True, blank=True)
    observacoes = models.TextField(null=True, blank=True)
    beneficiarios = models.TextField(null=True, blank=True)
    taxa = models.FloatField(null=True, blank=True)
    datacancelamento = models.DateField(null=True, blank=True)
    averbacao = models.DateField(null=True, blank=True)
    producao = models.DateField(null=True, blank=True)
    angariador = models.ForeignKey(Angariadores, on_delete=models.PROTECT, null=True, blank=True)
    clube = models.CharField(max_length=50, null=True, blank=True)
    nascimento = models.DateField(null=True, blank=True)
    tabela = models.CharField(max_length=50, null=True, blank=True)
    coluna = models.IntegerField(null=True, blank=True)
    anuencia = models.BooleanField(default=False)
    subconv = models.IntegerField(null=True, blank=True)
    tipo = models.CharField(max_length=10, null=True, blank=True)
    #beneficiariosNovos = models.ManyToManyField(BeneficiariosNovos, through="EducacionalBeneficiario", related_name="ApolicesE", blank=True)
    history = HistoricalRecords()
    def __str__(self):
        base = super().__str__()
        return base
