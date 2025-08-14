# views/a2055_views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from ..models import Clientes
from django import forms
from ..formsDir.apolices_decesso_Form import DecessoForm, Decesso

def decesso_create(request, pk):
    instancia = get_object_or_404(Clientes, pk=pk)
    if request.method == 'POST':
        form = DecessoForm(request.POST)
        form.instance.cliente = instancia
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro criado com sucesso!')
            return redirect('clientes')
        else:
            print(form.errors)
    else:
        
        form = DecessoForm()
        

    return render(request, 'form_decesso.html', {'form': form, 'title': 'Cadastro de Apólices DECESSO', 'cliente': instancia, 'novo':True})

def decesso_update(request, pk):
    instancia = get_object_or_404(Decesso, pk=pk)
    if request.method == 'POST':
        form = DecessoForm(request.POST, instance=instancia)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro alterado com sucesso!')
            return redirect('clientes')
        else:
            print(form.errors)
    else:
        form = DecessoForm(instance=instancia)
        form.fields['apolice'].widget = forms.HiddenInput()

    return render(request, 'form_decesso.html', {'form': form, 'title': 'Alteração de Apólices DECESSO', 'cliente':instancia.cliente, 'apolice':instancia, 'novo':False})
    

def decesso_impressao(request, pk):
    decesso = get_object_or_404(Decesso, pk=pk)
    return render(request, 'decesso_impressao.html', {'decesso': decesso})