import os
import django
import csv
from datetime import datetime

import pyodbc


# Configura o Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sisLeju.settings')  # <- ajuste aqui
django.setup()

from main.models import Angariadores


caminho_banco = r"C:\Users\Marcus\Downloads\listas.mdb"

# Conecta ao banco Access
conexao = pyodbc.connect(
        r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=' + caminho_banco + ';'
    )
cursor = conexao.cursor()
mapa1 = {'codigo': 1, 
            'nome': 2, 
            }
    
cursor.execute("SELECT * FROM angariadores")
dados = cursor.fetchall()
    
mapa = {}
for idx, coluna in enumerate(cursor.columns(table="angariadores")):
        col = coluna.column_name
        if col in mapa1:
            mapa[col]=idx

conexao.close()

for i in dados:
    print(i)
    Angariadores.objects.update_or_create(codigo=i[1], nome=i[2])
        
        

lista = Angariadores.objects.all()
for i in lista:
        print (i)
