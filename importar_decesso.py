import os
import django
import csv
from datetime import datetime
from importar_cliente import *
import pyodbc


# Configura o Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sisLeju.settings')  # <- ajuste aqui
django.setup()

from main.models import Clientes
from main.models import Decesso
from main.models import ApolicesGerais
from main.models import Angariadores

mapeamento_decesso = [ 
    'cliente',
    'apolice',
    'movimento',
    'inicio',
    'vigencia',
    'premio',
    'tipo',
    'taxa',
    'observacoes',
    'angariador',
    'datacancelamento',
    'producao',
    'averbacao',
    'clube',
    'anuencia',
    'subconv',
    'codunid',
]
caminho_banco = r"C:\Users\Marcus\Desktop\preencher_proposta\proposta\seguro\seguro.mdb"

# Conecta ao banco Access
conexao = pyodbc.connect(
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=' + caminho_banco + ';'
)

cursor = conexao.cursor()
mapa = {}
for idx, coluna in enumerate(cursor.columns(table="a2055")):
    col = coluna.column_name.replace('2055', '')
    col = col.lower()
    if col in mapeamento_decesso:
        mapa[col] = idx

cursor.execute("SELECT TOP 10 * FROM a2055 WHERE movimento2055 = 'A'")
dados = cursor.fetchall()
conexao.close()


for i in dados:
    dado = {}
    for d, e in mapa.items():
        if d=='tipo':d='segurotipo'
        dado[d] = i[e]
    
     
    cliente = Clientes.objects.filter(matricula = float(i[0]))
    
    
    
    if not cliente.exists():
        cl = pega_cliente(i[0])
        
        try:
            angariador = Angariadores.objects.get(codigo = cl['angariador'])
            Clientes.objects.update_or_create(
                cpf=cl.get('cpf'),
                angariador = angariador,
                defaults=cl
                )
        except:
            valor = cl.pop("angariador", None)
            Clientes.objects.update_or_create(
                cpf=cl.get('cpf'),
                defaults=cl
                )
    
    clienteatual = Clientes.objects.get(matricula = float(i[0]))
    apolice = ApolicesGerais.objects.get(nome = '2055')
    ang = int(dado.pop("angariador", None).split('-')[0])
    angariador = Angariadores.objects.get(codigo = ang)
    Decesso.objects.update_or_create(
        apolice = apolice,
        cliente = clienteatual,
        angariador = angariador,
        defaults=dado
    )
    
    

lista = Decesso.objects.all()
for i in lista:
    print (i)
