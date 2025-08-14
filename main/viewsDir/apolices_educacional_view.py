# views/a2055_views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from ..models import Clientes
from django import forms
from ..formsDir.apolices_educacionais_Form import ApolicesEForm, ApolicesE

def apolicesE_create(request, pk):
    instancia = get_object_or_404(Clientes, pk=pk)
    if request.method == 'POST':
        form = ApolicesEForm(request.POST)
        form.instance.cliente = instancia
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro criado com sucesso!')
            return redirect('clientes')
        else:
            print(form.errors)
    else:
        form = ApolicesEForm()
        

    return render(request, 'form_educ.html', {'form': form, 'title': 'Cadastro de Apólices EDUCACIONAL', 'cliente': instancia, 'novo':True})


def apolicesE_update(request, pk):
    instancia = get_object_or_404(ApolicesE, pk=pk)
    if request.method == 'POST':
        form = ApolicesEForm(request.POST, instance=instancia)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro alterado com sucesso!')
            return redirect('clientes')
    else:
        form = ApolicesEForm(instance=instancia)
        
        form.fields['apolice'].widget = forms.HiddenInput()

    return render(request, 'form_educ.html', {'form': form, 'title': 'Alteração de Apólices EDUCACIONAL', 'cliente':instancia.cliente, 'apolice':instancia})
    
