from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from ..models import Clientes
from django import forms
from ..formsDir.apolices_mulher_Form import ApolicesM, ApolicesMForm


def apolicesMulher_create(request, pk):
    instancia = get_object_or_404(Clientes, pk=pk)
    if request.method == 'POST':
        form = ApolicesMForm(request.POST)
        form.instance.cliente = instancia
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro criado com sucesso!')
            return redirect('clientes')
    else:
        form = ApolicesMForm()
        

    return render(request, 'form_mulher.html', {'form': form, 'title': 'Cadastro de Apólices MULHER', 'cliente': instancia, 'novo':True})

def apolicesMulher_update(request, pk):
    instancia = get_object_or_404(ApolicesM, pk=pk)
    if request.method == 'POST':
        form = ApolicesMForm(request.POST, instance=instancia)    
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro alterado com sucesso!')
            return redirect('clientes')
        else:
            print(form.errors)
    else:
        form = ApolicesMForm(instance=instancia)
        form.fields['apolice'].widget = forms.HiddenInput()

    return render(request, 'form_mulher.html', {'form': form, 'title': 'Alteração de Apólices MULHER', 'cliente':instancia.cliente, 'apolice':instancia, })
    

