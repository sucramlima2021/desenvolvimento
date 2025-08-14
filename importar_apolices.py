import os
import django
import csv
from datetime import datetime

# Configura o Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sisLeju.settings')  # <- ajuste aqui
django.setup()

from main.models import ApolicesGerais

# Mapeamento entre nomes do CSV e campos do model
APOLICES = {
    # tipo 'cifptd'
    '136403': 'cifptd',
    '136404': 'cifptd',
    '136402': 'cifptd',
    '136402A': 'cifptd',
    '136401': 'cifptd',

    # tipo 'sifptd'
    '136604': 'sifptd',
    '136603': 'sifptd',
    '136602': 'sifptd',
    '136601': 'sifptd',

    # tipo 'mulher'
    '137103': 'mulher',
    '137104': 'mulher',
    '137101': 'mulher',
    '137102': 'mulher',

    # tipo 'educacional'
    'Nova': 'educacional',
    '13': 'educacional',
    '14': 'educacional',
    
    '2055':'decesso',
    'Tokio Marine':'vida',
    'Tokio Marine':'residencia',
    'Tokio Marine':'carro',
    'Tokio Marine':'moto',
    'HDI':'residencia'
}


def importar_apolices():
    for nome, tipo in APOLICES.items():
        obj, created = ApolicesGerais.objects.get_or_create(
            nome=nome,
            defaults={
                'tipo': tipo,
                'observacoes': f'Importado automaticamente como tipo {tipo}.'
            }
        )
        if created:
            print(f'Criado: {obj}')
        else:
            print(f'Já existia: {obj}')

if __name__ == '__main__':
    importar_apolices()  # ajuste o nome do arquivo se necessário
