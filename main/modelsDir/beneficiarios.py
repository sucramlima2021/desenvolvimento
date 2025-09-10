from django.db import models

from .clientes import *
from .apolices_com_ifptd import *
from .apolices_sem_ifptd import *
from .apolices_mulher import *
from .apolices_educacional import *
from .apolices_geral import *
from simple_history.models import HistoricalRecords

class BeneficiariosNovos(models.Model):
    cliente = models.ForeignKey(Clientes, on_delete=models.PROTECT)
    apolice = models.ForeignKey(ApoliceBase, on_delete=models.PROTECT, null=True, blank=True)
    nome = models.CharField(max_length=50, null=True, blank=True)
    nascimento = models.DateTimeField(null=True, blank=True)
    cpf = models.CharField(max_length=11, null=True, blank=True)
    parentesco = models.CharField(max_length=30, null=True, blank=True)
    percentual = models.FloatField(null=True, blank=True)
    controle = models.CharField(max_length=10, null=True, blank=True)
    history = HistoricalRecords()
    def __str__(self):
        return str(f'{self.apolice} - {self.cliente} - {self.nome}')

'''class BeneficiariosNovos(models.Model): 
    nome = models.CharField(max_length=50, null=True, blank=True)
    nascimento = models.DateTimeField(null=True, blank=True)
    cpf = models.CharField(max_length=11, null=True, blank=True)
   
    def __str__(self):
        return str(f'{self.nome}')
    
class CifptdBeneficiario(models.Model):
    cifptd = models.ForeignKey(ApolicesCIFPTD, on_delete=models.CASCADE)
    beneficiario  = models.ForeignKey(BeneficiariosNovos, on_delete=models.CASCADE)
    parentesco = models.CharField(max_length=255, null=True, blank=True)
    percentual = models.IntegerField(null=True, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["cifptd", "beneficiario"], name="unique_person_group"
            )
        ]

class SifptdBeneficiario(models.Model):
    sifptd = models.ForeignKey(ApolicesSIFPTD, on_delete=models.CASCADE)
    beneficiario  = models.ForeignKey(BeneficiariosNovos, on_delete=models.CASCADE)
    parentesco = models.CharField(max_length=255, null=True, blank=True)
    percentual = models.IntegerField(null=True, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["sifptd", "beneficiario"], name="unique_person_group"
            )
        ]

class MulherBeneficiario(models.Model):
    mulher = models.ForeignKey(ApolicesM, on_delete=models.CASCADE)
    beneficiario  = models.ForeignKey(BeneficiariosNovos, on_delete=models.CASCADE)
    parentesco = models.CharField(max_length=255, null=True, blank=True)
    percentual = models.IntegerField(null=True, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["mulher", "beneficiario"], name="unique_person_group"
            )
        ]


class EducacionalBeneficiario(models.Model):
    educacional = models.ForeignKey(ApolicesE, on_delete=models.CASCADE)
    beneficiario  = models.ForeignKey(BeneficiariosNovos, on_delete=models.CASCADE)
    parentesco = models.CharField(max_length=255, null=True, blank=True)
    percentual = models.IntegerField(null=True, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["educacional", "beneficiario"], name="unique_person_group"
            )
        ]'''