import os
import django
import csv
from datetime import datetime

import pyodbc


def pega_cliente(cliente):
    caminho_banco = r"C:\Users\Marcus\Desktop\preencher_proposta\proposta\seguro\seguro.mdb"

# Conecta ao banco Access
    conexao = pyodbc.connect(
        r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=' + caminho_banco + ';'
    )
    cursor = conexao.cursor()
    mapa = {'matricula': 0, 
            'nome': 1, 
            'logradouro': 2, 
            'numero': 3, 
            'complemento': 4, 
            'bairro': 5, 
            'cidade': 6, 
            'uf': 7, 
            'segundoendereco': 8, 
            'telefone': 9, 
            'ramal': 10, 
            'fax': 11, 
            'ramalfax': 12, 
            'celulares': 13, 
            'rota': 14, 
            'localizador': 15, 
            'banco': 16, 
            'agencia': 17, 
            'cc': 18, 
            'email': 19, 
            'nascimento': 20, 
            'cpf': 21, 
            'identidade': 22, 
            'orgao': 23, 
            'expedicao': 24, 
            'estadocivil': 25, 
            'cargo': 26, 
            'funcao': 27, 
            'salario': 28, 
            'codunid': 29, 
            'angariador': 30, 
            'conjuge': 42, 
            'nascimentoconjuge': 43, 
            'cpfconjuge': 44, 
            'observacoes': 45, 
            'dco': 46, 
            'codconv': 47, 
            'subconv': 48, 
            'codclube': 49, 
            'codaverba': 50, 
            'sexo': 51, 
            'empresa': 52, 
            'cep': 53, 
            'anuencia': 54, 
            'correspondencia': 55, 
            'dataanuencia': 56, 
            'controle': 57, 
            'certificado': 59, 
            'angariadoranuencia': 60,  
            'caminho': 67, 
            'mat_antiga': 68, 
            'control_antigo': 69, 
            'codclube_antigo': 75, 
            'Anuencia_Antiga': 76}
    
    cursor.execute("SELECT * FROM clientes WHERE matricula = ?", (cliente,))
    dados = cursor.fetchone()
    
    if not dados:
        conexao.close()
        raise ValueError(f"Cliente com matrícula {cliente} não encontrado.")
    dd = {}
    for i, j in mapa.items():
        dd[i] = dados[j]
    conexao.close()
    return dd
    