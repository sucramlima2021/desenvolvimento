from django.db import models


class ApolicesGerais(models.Model):
    OPCOES_STATUS = [
        ('cifptd', 'CIFPTD'),
        ('sifptd', 'SIFPTD'),
        ('mulher', 'Mulher'),
        ('educacional', 'Educacional'),
    ]
    nome = models.CharField(max_length=255, unique=True)
    tipo = models.CharField(max_length=50, choices=OPCOES_STATUS, default='cifptd')
    observacoes = models.TextField()
    
    def __str__(self):
        return f'{self.tipo} - {self.nome}'


