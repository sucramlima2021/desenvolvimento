# views/a2055_views.py
from django.shortcuts import render, redirect, get_object_or_404
from ..models import BeneficiariosNovos
from ..formsDir.beneficiarios_Form import BeneficiariosForm
from django.contrib import messages
from ..models import Clientes
from django import forms
from .clientesView import *

def beneficiarios_create(request, pk):
    instancia = get_object_or_404(Clientes, pk=pk)
    if request.method == 'POST':
        form = BeneficiariosForm(request.POST, cliente=instancia)
        form.instance.cliente = instancia
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro criado com sucesso!')
            
            return redirect(seleciona_cliente, instancia.pk)
    else:
        form = BeneficiariosForm(cliente=instancia)
        

    return render(request, 'form_benef.html', {'form': form, 'title': 'Cadastro de Beneficiarios', 'cliente': instancia, 'novo':True})
    

def beneficiarios_update(request, pk):
    instancia = get_object_or_404(BeneficiariosNovos, pk=pk)
    cliente = instancia.cliente.pk
    if request.method == 'POST':
        form = BeneficiariosForm(request.POST, instance=instancia)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro alterado com sucesso!')
            return redirect(seleciona_cliente, cliente)
        else:
            # Se inválido, exibe erros no console (para debug)
            print(form.errors)  
    else:
        form = BeneficiariosForm(instance=instancia)
    return render(request, 'form_benef.html', {'form': form, 'title': 'Alteração de beneficiarios', 'cliente':instancia.cliente, "beneficiario":instancia, 'editar':True})
    
def beneficiarios_list(request, pk):
    cliente = get_object_or_404(Clientes, pk=pk)
    agregados = BeneficiariosNovos.objects.filter(cliente = cliente)
    
    return render(request, 'list_benef.html', {'title': 'Listagem de Agregados', 'cliente':cliente, 'registro':agregados})

def beneficiarios_delete(request, pk):
    apolice = BeneficiariosNovos.objects.get(id = pk)
    cliente = apolice.cliente.pk
    if apolice:
        try:
            apolice.delete()
        except:
            messages.error(request, "Não foi possível apagar este beneficiario. Existem registros vinculados a ele.")
            previous_url = request.META.get('HTTP_REFERER', '/')
            return redirect(previous_url)
    return redirect(seleciona_cliente, cliente)