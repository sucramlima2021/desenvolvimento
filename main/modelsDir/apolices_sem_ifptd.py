from django.db import models

from .clientes import *
from .apolices_geral import *
from .beneficiarios import *
from .angariadores import *

class ApolicesSIFPTD(ApoliceBase):
    STATUS_CHOICES = [
        ('', 'Nenhum'),  # valor vazio para "nenhum"
        ('A', 'Ativo'),
        ('C', 'Cancelado'),
        ('S', 'Sinistrado'),
    ]
    movimentoconjuge = models.CharField(max_length=1, choices = STATUS_CHOICES, null=True, blank=True)
    datacancelamento = models.DateField(null=True, blank=True)
    datacancelamentoconjuge = models.DateField(null=True, blank=True)
    averbacao = models.DateField(null=True, blank=True)
    averbacaoconjuge = models.DateField(null=True, blank=True)
    producao = models.DateField(null=True, blank=True)
    producaoconjuge = models.DateField(null=True, blank=True)
    inicioconjuge = models.DateField(null=True, blank=True)
    premioconjuge = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    isbasica = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    isbasicaconjuge = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    iea = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    ieaconjuge = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    ipa = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    ipaconjuge = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    observacoes = models.TextField(null=True, blank=True)
    beneficiarios = models.TextField(null=True, blank=True)
    taxa = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True)
    taxaconjuge = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True)
    vigenciaconjuge = models.DateField(null=True, blank=True)
    angariador = models.ForeignKey(Angariadores, on_delete=models.PROTECT, null=True, blank=True)
    clube = models.CharField(max_length=50, null=True, blank=True)
    anuencia = models.BooleanField(null=True, blank=True)
    anuenciaconjuge = models.BooleanField(null=True, blank=True)
    subconv = models.IntegerField(null=True, blank=True)
    codunid = models.IntegerField(null=True, blank=True)
    segurotipoconj = models.CharField(max_length=10, null=True, blank=True)
    #beneficiariosNovos = models.ManyToManyField(BeneficiariosNovos, through="SifptdBeneficiario", related_name="ApolicesSIFPTD", blank=True)
    
    def __str__(self):
        base = super().__str__()
        return base