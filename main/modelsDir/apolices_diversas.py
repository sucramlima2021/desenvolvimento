from django.db import models
from .clientes import *
from .apolices_geral import *


class ApolicesVida(ApoliceBase):
    ramo = models.CharField(max_length=50, null=True, blank=True)
    apolicenumero = models.IntegerField(null=True, blank=True)
    plano = models.IntegerField(null=True, blank=True)
    proposta = models.IntegerField(null=True, blank=True) 
    emissao = models.DateTimeField(null=True, blank=True)
    referencia = models.DateTimeField(null=True, blank=True)
    isbasica = models.FloatField(null=True, blank=True)
    dataCancelamento = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        base = super().__str__()
        return base

class ApolicesResidencia(ApoliceBase):
    ramo = models.CharField(max_length=50, null=True, blank=True)
    apolicenumero = models.IntegerField(null=True, blank=True)
    negocio = models.IntegerField(null=True, blank=True)
    item = models.IntegerField(null=True, blank=True) 
    classeBonus = models.IntegerField(null=True, blank=True) 
    emissao = models.DateTimeField(null=True, blank=True)
    versao = models.DateTimeField(null=True, blank=True)
    tipoConstrucao = models.CharField(max_length=100, null=True, blank=True)
    tipoImovel = models.CharField(max_length=100, null=True, blank=True)
    ocupacao = models.CharField(max_length=100, null=True, blank=True)
    endereco = models.CharField(max_length=255, null=True, blank=True)
    numero = models.IntegerField(null=True, blank=True)
    complemento = models.CharField(max_length=255, null=True, blank=True)
    bairro = models.CharField(max_length=255, null=True, blank=True)
    cidade = models.CharField(max_length=255, null=True, blank=True)
    cep = models.CharField(max_length=20, null=True, blank=True)
    uf = models.CharField(max_length=10, null=True, blank=True)
    tipoindenizacao = models.CharField(max_length=255, null=True, blank=True)
    limite = models.FloatField(null=True, blank=True)
    dataCancelamento = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        base = super().__str__()
        return base
    

class ApolicesMoto(ApoliceBase):
    ramo = models.CharField(max_length=50, null=True, blank=True)
    apolicenumero = models.IntegerField(null=True, blank=True)
    negocio = models.IntegerField(null=True, blank=True)
    proposta = models.IntegerField(null=True, blank=True) 
    ci = models.IntegerField(null=True, blank=True) 
    classeBonus = models.IntegerField(null=True, blank=True) 
    emissao = models.DateTimeField(null=True, blank=True)
    versao = models.DateTimeField(null=True, blank=True)
    condutor = models.CharField(max_length=255, null=True, blank=True)
    cpfCondutor = models.CharField(max_length=100, null=True, blank=True)
    estadoCivilCondutor = models.CharField(max_length=100, null=True, blank=True)
    
    veiculo = models.CharField(max_length=100, null=True, blank=True)
    fabricante = models.CharField(max_length=100, null=True, blank=True)
    ano = models.IntegerField(null=True, blank=True)
    chassi = models.CharField(max_length=255, null=True, blank=True)
    placa = models.CharField(max_length=50, null=True, blank=True)
    tipoUtilizacao = models.CharField(max_length=100, null=True, blank=True)
    fipe = models.CharField(max_length=100, null=True, blank=True)
    
    cep = models.CharField(max_length=100, null=True, blank=True)
    tipoResidencia = models.CharField(max_length=100, null=True, blank=True)
    garagem = models.CharField(max_length=255, null=True, blank=True)
    
    limite = models.FloatField(null=True, blank=True)
    dataCancelamento = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        base = super().__str__()
        return base

class ApolicesCarro(ApoliceBase):
    ramo = models.CharField(max_length=50, null=True, blank=True)
    apolicenumero = models.IntegerField(null=True, blank=True)
    negocio = models.IntegerField(null=True, blank=True)
    proposta = models.IntegerField(null=True, blank=True) 
    ci = models.IntegerField(null=True, blank=True) 
    classeBonus = models.IntegerField(null=True, blank=True) 
    emissao = models.DateTimeField(null=True, blank=True)
    versao = models.DateTimeField(null=True, blank=True)
    condutor = models.CharField(max_length=255, null=True, blank=True)
    cpfCondutor = models.CharField(max_length=100, null=True, blank=True)
    estadoCivilCondutor = models.CharField(max_length=100, null=True, blank=True)
    
    veiculo = models.CharField(max_length=100, null=True, blank=True)
    fabricante = models.CharField(max_length=100, null=True, blank=True)
    ano = models.IntegerField(null=True, blank=True)
    chassi = models.CharField(max_length=255, null=True, blank=True)
    placa = models.CharField(max_length=50, null=True, blank=True)
    tipoUtilizacao = models.CharField(max_length=100, null=True, blank=True)
    fipe = models.CharField(max_length=100, null=True, blank=True)
    
    cep = models.CharField(max_length=100, null=True, blank=True)
    tipoResidencia = models.CharField(max_length=100, null=True, blank=True)
    garagem = models.CharField(max_length=255, null=True, blank=True)
    
    limite = models.FloatField(null=True, blank=True)
    dataCancelamento = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        base = super().__str__()
        return base