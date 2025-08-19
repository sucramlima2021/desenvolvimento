from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.core.paginator import Paginator
from django.db.models import Q
from ..modelsDir.sinistros import Sinistros
from ..formsDir.sinistros_form import SinistrosForm
from ..modelsDir.clientes import *

def sinistros_list(request):
    qs = Sinistros.objects.select_related("cliente", "apolice").all().order_by("-data", "-id")
    q = request.GET.get("q", "").strip()
    status = request.GET.get("status", "").strip()  # 'pago' | 'pendente' | ''
    if q:
        qs = qs.filter(
            Q(cliente__nome__icontains=q) |
            Q(apolice__nome__icontains=q) |
            Q(tipo__icontains=q) |
            Q(nome_segurado__icontains=q) |
            Q(cpf_segurado__icontains=q) |
            Q(controle__icontains=q)
        )
    if status == "pago":
        qs = qs.filter(pago_recusa=True)
    elif status == "pendente":
        qs = qs.filter(Q(pago_recusa=False) | Q(pago_recusa__isnull=True))

    paginator = Paginator(qs, 20)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "sinistros_list.html", {
        "sinistros": page_obj.object_list,
        "page_obj": page_obj,
        "is_paginated": page_obj.paginator.num_pages > 1,
        "paginator": paginator,
        "request": request,
    })

def sinistros_create(request, pk):
    cliente = get_object_or_404(Clientes, pk=pk)
    if request.method == "POST":
        form = SinistrosForm(request.POST, cliente=cliente)
        form.instance.cliente = cliente
        if form.is_valid():
            form.save()
            return redirect("sinistros_list")
    else:
        form = SinistrosForm(cliente=cliente)
    return render(request, "form_sinistro.html", {"form": form, 'cliente':cliente})

def sinistros_update(request, pk):
    obj = get_object_or_404(Sinistros, pk=pk)
    if request.method == "POST":
        form = SinistrosForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("sinistros_list")
    else:
        form = SinistrosForm(instance=obj)
    return render(request, "form_sinistro.html", {"form": form, "object": obj, "editar":True})

def sinistros_delete(request, pk):
    obj = get_object_or_404(Sinistros, pk=pk)
    if request.method == "POST":
        obj.delete()
        return redirect("sinistros_list")
    return render(request, "sinistros_confirm_delete.html", {"object": obj})
