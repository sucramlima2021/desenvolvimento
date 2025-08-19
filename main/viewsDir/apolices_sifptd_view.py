# views/a2055_views.py
from django.shortcuts import render, redirect, get_object_or_404
from ..formsDir.apolices_sifptd_Form import ApolicesSIFPTD, ApolicesSIFPTDForm
from django.contrib import messages
from ..models import Clientes
from django import forms
from .clientesView import *

def apolicesSIFPTD_create(request, pk):
    instancia = get_object_or_404(Clientes, pk=pk)
    if request.method == 'POST':
        form = ApolicesSIFPTDForm(request.POST)
        form.instance.cliente = instancia
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro criado com sucesso!')
            return redirect(seleciona_cliente, instancia.pk)
        else:
            print(form.errors)
    else:
        form = ApolicesSIFPTDForm()
        

    return render(request, 'form_cifptd.html', {'form': form, 'title': 'Cadastro de Apólices SIFPTD', 'cliente': instancia, 'novo':True})

def apolicesSIFPTD_update(request, pk):
    instancia = get_object_or_404(ApolicesSIFPTD, pk=pk)
    if request.method == 'POST':
        form = ApolicesSIFPTDForm(request.POST, instance=instancia)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro alterado com sucesso!')
            return redirect(seleciona_cliente, instancia.cliente.pk)
    else:
        form = ApolicesSIFPTDForm(instance=instancia)
        form.fields['apolice'].widget = forms.HiddenInput()

    return render(request, 'form_sifptd.html', {'form': form, 'title': 'Alteração de Apólices SIFPTD', 'cliente':instancia.cliente, 'apolice':instancia, "editar":True})
    
def apolicesSIFPTD_delete(request, pk):
    apolice = ApolicesSIFPTD.objects.get(id = pk)
    cliente = apolice.cliente.pk
    if apolice:
        try:
            apolice.delete()
        except:
            messages.error(request, "Não foi possível apagar este apolice. Existem registros vinculados a ela.")
            previous_url = request.META.get('HTTP_REFERER', '/')
            return redirect(previous_url)
    return redirect(seleciona_cliente, cliente)