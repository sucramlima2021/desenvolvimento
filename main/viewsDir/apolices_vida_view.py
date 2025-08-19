from django.shortcuts import render, redirect, get_object_or_404
from django.core.files.storage import default_storage
from django.contrib import messages
from ..models import Clientes
from django import forms
from ..formsDir.apolices_diversas_form import *
from .clientesView import *
import pdfplumber
from ..utilidades.extrai_pdf_vida_tokio import extrair_dados_pdf
from datetime import datetime


def apolicesVida_create(request, pk):
    instancia = get_object_or_404(Clientes, pk=pk)
    if request.method == 'POST':
        form = ApolicesVidaForm(request.POST)
        form.instance.cliente = instancia
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro criado com sucesso!')
            return redirect(seleciona_cliente, instancia.pk)
    else:
        form = ApolicesVidaForm()
    return render(request, 'form_vida.html', {'form': form, 'title': 'Cadastro de Apólices Vida', 'cliente': instancia, 'novo':True})

def apolicesVida_update(request, pk):
    instancia = get_object_or_404(ApolicesVida, pk=pk)
    if request.method == 'POST':
        form = ApolicesVidaForm(request.POST, instance=instancia)    
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro alterado com sucesso!')
            return redirect(seleciona_cliente, instancia.cliente.pk)
        else:
            print(form.errors)
    else:
        form = ApolicesVidaForm(instance=instancia)
        form.fields['apolice'].widget = forms.HiddenInput()
    return render(request, 'form_vida.html', {'form': form, 'title': 'Alteração de Apólices Vida', 'cliente':instancia.cliente, 'apolice':instancia, "editar":True })
    
def apolicesVida_delete(request, pk):
    apolice = get_object_or_404(ApolicesVida, pk=pk)
    cliente = apolice.cliente.pk
    if apolice:
        try:
            apolice.delete()
        except:
            messages.error(request, "Não foi possível apagar este apolice. Existem registros vinculados a ela.")
            previous_url = request.META.get('HTTP_REFERER', '/')
            return redirect(previous_url)
    return redirect(seleciona_cliente, cliente)




def upload_pdf_vida(request):
    
    if request.method == "POST" and request.FILES.get("arquivo_pdf"):
        arquivo = request.FILES["arquivo_pdf"]

        # salvar temporariamente
        caminho_temp = default_storage.save(arquivo.name, arquivo)

        try:
            # abrir PDF
            with pdfplumber.open(default_storage.path(caminho_temp)) as pdf:
                texto = "\n".join(page.extract_text() or "" for page in pdf.pages)

            dados = extrair_dados_pdf(default_storage.path(caminho_temp))
            cliente = Clientes.objects.update_or_create(
                nome = dados['segurado'],
                cpf = dados['cpf'],
                logradouro = dados['endereco'],
                bairro = dados['bairro'],
                cidade = dados['cidade'],
                uf = dados['uf'],
                cep = dados['cep'],
                celulares = dados['celular']
            )
            clienteatual = Clientes.objects.get(cpf = dados['cpf'])
            apolice = ApolicesGerais.objects.get(nome = 'Tokio Marine', tipo = 'vida')
            reg = ApolicesVida.objects.update_or_create(
                cliente = clienteatual,
                apolice = apolice,
                movimento = 'A',
                inicio = datetime.strptime(dados['data_inicio_vigencia'], "%d/%m/%Y").date(),
                vigencia = datetime.strptime(dados['data_fim_vigencia'], "%d/%m/%Y").date(),
                premio = float(dados['premio_liquido_total'].replace(".", "").replace(",", ".")),
                segurotipo = dados['tipo_seguro'],
                ramo = dados['ramo'],
                apolicenumero = dados['apolice'],
                plano = dados['plano'],
                proposta = dados['proposta'] ,
                emissao = datetime.strptime(dados['data_emissao'], "%d/%m/%Y").date(), 
                referencia = datetime.strptime(dados['data_referencia'], "%d/%m/%Y").date(),
                isbasica = float(dados['valor_cobertura_basica'].replace(".", "").replace(",", "."))
            )

        finally:
            # garantir que o arquivo será removido após a leitura
            if default_storage.exists(caminho_temp):
                default_storage.delete(caminho_temp)
        print(dados)
    return redirect('dashboard')


