from django.db import models
from ..models import Clientes


class ApolicesGerais(models.Model):
    TIPOS = [
        ('cifptd', 'CIFPTD'),
        ('sifptd', 'SIFPTD'),
        ('mulher', 'Mulher'),
        ('educacional', 'Educacional'),
        ('decesso', 'Decesso'),
        ('vida', 'Vida'),
        ('residencia', 'Residência'),
        ('moto', 'Moto'),
        ('carro', 'Carro'), 
    ]
    nome = models.CharField(max_length=255)
    tipo = models.CharField(max_length=50, choices=TIPOS, default='cifptd', db_index=True)
    observacoes = models.TextField(blank=True, null=True)
    
    class Meta:
        verbose_name = "Apólice (catálogo)"
        verbose_name_plural = "Apólices (catálogo)"
        constraints = [
            models.UniqueConstraint(fields=['tipo', 'nome'], name='uniq_tipo_nome')
        ]
    
    def __str__(self):
        return f'{self.get_tipo_display()} - {self.nome}'


class ApoliceBase(models.Model):
    STATUS_CHOICES = [
        ('', 'Nenhum'),  # valor vazio para "nenhum"
        ('A', 'Ativo'),
        ('C', 'Cancelado'),
        ('S', 'Sinistrado'),
    ]
    cliente = models.ForeignKey(Clientes, on_delete=models.PROTECT, related_name='apolices')
    apolice = models.ForeignKey(ApolicesGerais, on_delete=models.PROTECT, related_name='instancias')
    movimento = models.CharField(max_length=1, choices = STATUS_CHOICES, null=True, blank=True)
    inicio = models.DateField(null=True, blank=True)
    vigencia = models.DateField(null=True, blank=True)
    premio = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    segurotipo = models.CharField(max_length=50, null=True, blank=True)
    
    class Meta:
        verbose_name = "Apólice"
        verbose_name_plural = "Apólices"

    def __str__(self):
        # cuidado: acessar cliente.nome pode gerar N+1; use select_related('cliente') ao listar
        return f"{self.apolice}"