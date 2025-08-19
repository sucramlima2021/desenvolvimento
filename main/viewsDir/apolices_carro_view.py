from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from ..models import Clientes
from django import forms
from ..formsDir.apolices_diversas_form import *
from .clientesView import *


def apolicesCarro_create(request, pk):
    instancia = get_object_or_404(Clientes, pk=pk)
    if request.method == 'POST':
        form = ApolicesCarroForm(request.POST)
        form.instance.cliente = instancia
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro criado com sucesso!')
            return redirect(seleciona_cliente, instancia.pk)
    else:
        form = ApolicesCarroForm()
    return render(request, 'form_carro.html', {'form': form, 'title': 'Cadastro de Apólices Carro', 'cliente': instancia, 'novo':True})

def apolicesCarro_update(request, pk):
    instancia = get_object_or_404(ApolicesCarro, pk=pk)
    if request.method == 'POST':
        form = ApolicesCarroForm(request.POST, instance=instancia)    
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro alterado com sucesso!')
            return redirect(seleciona_cliente, instancia.cliente.pk)
        else:
            print(form.errors)
    else:
        form = ApolicesCarroForm(instance=instancia)
        form.fields['apolice'].widget = forms.HiddenInput()
    return render(request, 'form_carro.html', {'form': form, 'title': 'Alteração de Apólices Carro', 'cliente':instancia.cliente, 'apolice':instancia, "editar":True })
    
def apolicesCarro_delete(request, pk):
    apolice = get_object_or_404(ApolicesCarro, pk=pk)
    cliente = apolice.cliente.pk
    if apolice:
        try:
            apolice.delete()
        except:
            messages.error(request, "Não foi possível apagar este apolice. Existem registros vinculados a ela.")
            previous_url = request.META.get('HTTP_REFERER', '/')
            return redirect(previous_url)
    return redirect(seleciona_cliente, cliente)