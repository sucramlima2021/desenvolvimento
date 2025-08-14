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
from main.models import ApolicesCIFPTD
from main.models import ApolicesGerais
from main.models import Angariadores

mapeamento_cifptd = {
    
    "movimento":1, 
    "movimentoconjuge":3, 
    "datacancelamento":4, 
    "datacancelamentoconjuge":5, 
    "averbacao":6, 
    "averbacaoconjuge":7, 
    "producao":8, 
    "producaoconjuge":9, 
    "inicio":10, 
    "inicioconjuge":11, 
    "premio":12, 
    "premioconjuge":13, 
    "isbasica":14, 
    "isbasicaconjuge":15, 
    "iea":16, 
    "ieaconjuge":17, 
    "ipa":18, 
    "ipaconjuge":19, 
    "ifptd":20, 
    "ifptdconjuge":21, 
    "observacoes":22, 
    "beneficiarios":23, 
    "taxa":24, 
    "taxaconjuge":25, 
    "vigencia":26, 
    "vigenciaconjuge":27,  
    "clube":29, 
    "tabela":36, 
    "coluna":37, 
    "tabelaconjuge":38, 
    "colunaconjuge":39, 
    "subconv":40, 
    "codunid":41, 
    "segurotipo":42, 
    "segurotipoconj":44, 
}
caminho_banco = r"C:\Users\Marcus\Desktop\preencher_proposta\proposta\seguro\seguro.mdb"

# Conecta ao banco Access
conexao = pyodbc.connect(
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=' + caminho_banco + ';'
)

cursor = conexao.cursor()
cursor.execute("SELECT TOP 10 * FROM a136404 WHERE movimento136404 = 'A'")
dados = cursor.fetchall()


conexao.close()

for i in dados:
    dado = {}
    for d, e in mapeamento_cifptd.items():
        
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
    apolice = ApolicesGerais.objects.get(nome = '136404')
    angariador = Angariadores.objects.get(codigo = i[28].split('-')[0])
    ApolicesCIFPTD.objects.update_or_create(
        apolice = apolice,
        cliente = clienteatual,
        angariador = angariador,
        defaults=dado
    )
    
    

lista = ApolicesCIFPTD.objects.all()
for i in lista:
    print (i)
