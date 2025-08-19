import pdfplumber
import re

def extrair_dados_pdf(caminho_pdf):
    dados = {}

    with pdfplumber.open(caminho_pdf) as pdf:
        texto = "\n".join(page.extract_text() or "" for page in pdf.pages)

    # ------------------------------
    # Dados pessoais do segurado
    # ------------------------------
    dados['segurado'] = re.search(r"Segurado:\s*(.+)", texto)
    dados['cpf'] = re.search(r"CPF:\s*([\d\.\-]+)", texto)
    dados['data_nasc'] = re.search(r"Data de Nasc\.\:\s*([\d/]+)", texto)
    dados['endereco'] = re.search(r"Endereço:\s*(.+)", texto)
    dados['bairro'] = re.search(r"Bairro:\s*([^\n]+)", texto)
    dados['cep'] = re.search(r"CEP:\s*([\d\-]+)", texto)
    dados['cidade'] = re.search(r"Cidade:\s*([^\n]+)", texto)
    dados['uf'] = re.search(r"UF:\s*([A-Z]{2})", texto)
    dados['celular'] = re.search(r"Celular:\s*([\(\)\d\s\-]+)", texto)
    
    # ------------------------------
    # Coberturas
    # ------------------------------
    dados['valor_cobertura_basica'] = re.search(r"BÁSICA \(MORTE\)\s*([\d\.\,]+)", texto)
    dados['premio_liquido_total'] = re.search(r"Prêmio Líquido Total:\s*R\$ ([\d\.\,]+)", texto)

    # ------------------------------
    # Dados do contrato
    # ------------------------------
    dados['vigencia'] = re.search(r"Vigência:\s*a partir das 24 horas do dia ([\d/]+) até as 24 horas do dia ([\d/]+)", texto)
    dados['ramo'] = re.search(r"Ramo:\s*([\d\.]+)", texto)
    dados['apolice'] = re.search(r"Apólice:\s*(\d+)", texto)
    dados['plano'] = re.search(r"Plano:\s*(\d+)", texto)
    dados['proposta'] = re.search(r"Proposta:\s*(\d+)", texto)
    dados['tipo_seguro'] = re.search(r"Tipo de Seguro:\s*([^\n]+)", texto)
    dados['data_emissao'] = re.search(r"Data da Emissão:\s*([\d/]+)", texto)
    dados['data_referencia'] = re.search(r"Data da Referência:\s*([\d/]+)", texto)

    # ------------------------------
    # Beneficiários (lista corrigida)
    # ------------------------------
    beneficiarios = []
    linhas = texto.splitlines()

    for i, linha in enumerate(linhas):
        m = re.search(r"(\d{2}/\d{2}/\d{4})\s+([^\d\n]+?)\s+([\d,]+)", linha)
        if m and i > 0:
            nome = linhas[i-1].strip()
            beneficiarios.append({
                "nome": nome,
                "data_nasc": m.group(1).strip(),
                "parentesco": m.group(2).strip(),
                "percentual": m.group(3).strip()
            })

    dados['beneficiarios'] = beneficiarios

    # ------------------------------
    # Normalizar os resultados
    # ------------------------------
    for chave, valor in list(dados.items()):
        if chave not in ['beneficiarios']:
            if valor:
                if chave == 'vigencia':
                    dados['data_inicio_vigencia'] = valor.group(1).strip()
                    dados['data_fim_vigencia'] = valor.group(2).strip()
                    del dados['vigencia']
                else:
                    dados[chave] = valor.group(1).strip()
            else:
                dados[chave] = None

    return dados

    