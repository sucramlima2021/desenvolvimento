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
from main.models import ApolicesSIFPTD
from main.models import ApolicesGerais
from main.models import Angariadores

mapeamento_sifptd = [ 
    'movimento', 
    'movimentoconjuge', 
    'datacancelamento', 
    'datacancelamentoconjuge', 
    'averbacao', 
    'averbacaoconjuge', 
    'producao', 
    'producaoconjuge', 
    'inicio', 
    'inicioconjuge', 
    'premio', 
    'premioconjuge', 
    'isbasica', 
    'isbasicaconjuge', 
    'iea', 
    'ieaconjuge', 
    'ipa', 
    'ipaconjuge', 
    'observacoes', 
    'beneficiarios', 
    'taxa', 
    'taxaconjuge', 
    'vigencia', 
    'vigenciaconjuge', 
    'angariador', 
    'clube', 
    'anuencia', 
    'anuenciaconjuge', 
    'subconv', 
    'codunid', 
    'tipo', 
    'tipoconj', 
]
caminho_banco = r"C:\Users\Marcus\Desktop\preencher_proposta\proposta\seguro\seguro.mdb"

# Conecta ao banco Access
conexao = pyodbc.connect(
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=' + caminho_banco + ';'
)

cursor = conexao.cursor()
mapa = {}
for idx, coluna in enumerate(cursor.columns(table="a136604")):
    col = coluna.column_name.replace('136604', '')
    col = col.lower()
    if col in mapeamento_sifptd:
        mapa[col] = idx

cursor.execute("SELECT TOP 10 * FROM a136604 WHERE movimento136604 = 'A'")
dados = cursor.fetchall()
conexao.close()


for i in dados:
    dado = {}
    for d, e in mapa.items():
        if d=='tipo':d='segurotipo'
        if d=='tipoconj':d='segurotipoconj'
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
    apolice = ApolicesGerais.objects.get(nome = '136604')
    ang = int(dado.pop("angariador", None).split('-')[0])
    angariador = Angariadores.objects.get(codigo = ang)
    ApolicesSIFPTD.objects.update_or_create(
        apolice = apolice,
        cliente = clienteatual,
        angariador = angariador,
        defaults=dado
    )
    
    

lista = ApolicesSIFPTD.objects.all()
for i in lista:
    print (i)
