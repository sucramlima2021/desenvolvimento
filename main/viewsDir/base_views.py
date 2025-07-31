# base_views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib import messages

def base_list_view(request, model, template_name, titulo, campos_visiveis, url_edicao, url_novo, search_fields=None, paginate_by=10, url_apagar = False):
    """
    View base para listar registros com busca e paginação.
    """
    query = request.GET.get('q')
    registros = model.objects.all()

    if query and search_fields:
        q_objects = Q()
        for field in search_fields:
            q_objects |= Q(**{f"{field}__icontains": query})
        registros = registros.filter(q_objects)

    # Paginação
    paginator = Paginator(registros, paginate_by)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    campos_busca = ", ".join([field.capitalize() for field in search_fields]) if search_fields else ""

      
    context = {
        'page_obj': page_obj,
        'registros': page_obj.object_list,
        'query': query,
        'title': titulo,
        'campos_visiveis': campos_visiveis,
        'url_edicao': url_edicao,
        'url_novo': url_novo,
        'url_apagar': url_apagar,
        'campos_busca': campos_busca
    }
    return render(request, template_name, context)


def base_create_view(request, form_class, success_url, template_name, titulo, success_message='Criado com sucesso!'):
    """
    View base para criar registros, com login obrigatório e mensagens de sucesso.
    """
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, success_message)
            return redirect(success_url)
    else:
        form = form_class()

    return render(request, template_name, {'form': form, 'back_url': success_url, 'title': titulo})


def base_update_view(request, pk, model, form_class, success_url, template_name, titulo, success_message='Atualizado com sucesso!'):
    """
    View base para editar registros, com login obrigatório e mensagens de sucesso.
    """
    instancia = get_object_or_404(model, pk=pk)

    if request.method == 'POST':
        form = form_class(request.POST, instance=instancia)
        if form.is_valid():
            form.save()
            messages.success(request, success_message)
            return redirect(success_url)
    else:
        form = form_class(instance=instancia)

    return render(request, template_name, {'form': form, 'back_url': success_url, 'title': titulo})
