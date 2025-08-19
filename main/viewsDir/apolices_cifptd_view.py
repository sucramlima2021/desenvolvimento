# views/a2055_views.py
from django.shortcuts import render, redirect, get_object_or_404
from .base_views import base_list_view, base_create_view, base_update_view
from ..formsDir.apolices_cifptd_Form import ApolicesCIFPTD, ApolicesCIFPTDForm
from django.contrib import messages
from ..models import Clientes
from .clientesView import *
from django import forms

def apolicesCIFPTD_create(request, pk):
    instancia = get_object_or_404(Clientes, pk=pk)
    if request.method == 'POST':
        form = ApolicesCIFPTDForm(request.POST)
        form.instance.cliente = instancia
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro criado com sucesso!')
            
            return redirect(seleciona_cliente, instancia.pk)
    else:
        form = ApolicesCIFPTDForm()
        

    return render(request, 'form_cifptd.html', {'form': form, 'title': 'Cadastro de Apólices CIFPTD', 'cliente': instancia, 'novo':True})
    

def apolicesCIFPTD_update(request, pk):
    instancia = get_object_or_404(ApolicesCIFPTD, pk=pk)
    
    
    if request.method == 'POST':
        form = ApolicesCIFPTDForm(request.POST, instance=instancia)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro alterado com sucesso!')
            return redirect(seleciona_cliente, instancia.cliente.pk)
        else:
            # Se inválido, exibe erros no console (para debug)
            print(form.errors)  
    else:
        form = ApolicesCIFPTDForm(instance=instancia)
        form.fields['apolice'].widget = forms.HiddenInput()
        

    return render(request, 'form_cifptd.html', {'form': form, 'title': 'Alteração de Apólices CIFPTD', 'cliente':instancia.cliente, 'apolice':instancia, "editar":True})
    
def apolicesCIFPTD_delete(request, pk):
    apolice = ApolicesCIFPTD.objects.get(id = pk)
    cliente = apolice.cliente.pk
    if apolice:
        try:
            apolice.delete()
        except:
            messages.error(request, "Não foi possível apagar este apolice. Existem registros vinculados a ela.")
            previous_url = request.META.get('HTTP_REFERER', '/')
            return redirect(previous_url)
    return redirect(seleciona_cliente, cliente)