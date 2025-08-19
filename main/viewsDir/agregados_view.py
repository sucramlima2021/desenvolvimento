# views/a2055_views.py
from django.shortcuts import render, redirect, get_object_or_404
from ..models import Agregados
from ..formsDir.agregados_Form import AgregadosForm
from django.contrib import messages
from ..models import Clientes
from django import forms
from .clientesView import *

def agregados_create(request, pk):
    instancia = get_object_or_404(Clientes, pk=pk)
    if request.method == 'POST':
        form = AgregadosForm(request.POST)
        form.instance.cliente = instancia
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro criado com sucesso!')
            
            return redirect(seleciona_cliente, instancia.pk)
    else:
        form = AgregadosForm()
        

    return render(request, 'form_agregados.html', {'form': form, 'title': 'Cadastro de Agregados', 'cliente': instancia, 'novo':True})
    

def agregados_update(request, pk):
    instancia = get_object_or_404(Agregados, pk=pk)
    cliente = instancia.cliente.pk
    if request.method == 'POST':
        form = AgregadosForm(request.POST, instance=instancia)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro alterado com sucesso!')
            return redirect(seleciona_cliente, cliente)
        else:
            # Se inválido, exibe erros no console (para debug)
            print(form.errors)  
    else:
        form = AgregadosForm(instance=instancia)
    return render(request, 'form_agregados.html', {'form': form, 'title': 'Alteração de Apólices CIFPTD', 'cliente':instancia.cliente, "agregado":instancia, 'editar':True})
    
def agregados_list(request, pk):
    cliente = get_object_or_404(Clientes, pk=pk)
    agregados = Agregados.objects.filter(cliente = cliente)
    print(agregados)
    return render(request, 'list_agregados.html', {'title': 'Listagem de Agregados', 'cliente':cliente, 'registro':agregados})

def agregados_delete(request, pk):
    apolice = Agregados.objects.get(id = pk)
    cliente = apolice.cliente.pk
    if apolice:
        try:
            apolice.delete()
        except:
            messages.error(request, "Não foi possível apagar este apolice. Existem registros vinculados a ela.")
            previous_url = request.META.get('HTTP_REFERER', '/')
            return redirect(previous_url)
    return redirect(seleciona_cliente, cliente)