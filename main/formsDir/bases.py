# forms/bases.py (por exemplo)
from django import forms
from django_select2.forms import ModelSelect2Widget
from collections import OrderedDict
from ..modelsDir.clientes import Clientes

class ClienteSelectWidget(ModelSelect2Widget):
    model = Clientes
    search_fields = ['nome__icontains', 'cpf__icontains']

    def label_from_instance(self, obj):
        return f'{obj.cpf} - {obj.nome}'

class BaseClienteForm(forms.ModelForm):
    """Formulário base para modelos que têm um campo 'cliente'."""

    cliente_field_name = 'cliente'  # nome do campo que referencia o cliente

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        cliente_field = self.cliente_field_name

        if self.instance and self.instance.pk:
            # Se for edição, exibir campo readonly
            cliente_obj = getattr(self.instance, cliente_field)
            self.fields[f'{cliente_field}_label'] = forms.CharField(
                label='Cliente',
                initial=f'{cliente_obj.cpf} - {cliente_obj.nome}',
                required=False,
                disabled=True,
                widget=forms.TextInput(attrs={'class': 'form-control-plaintext', 'readonly': 'readonly'})
            )
            del self.fields[cliente_field]

            # Reordenar campos: colocar label primeiro
            new_fields = OrderedDict()
            new_fields[f'{cliente_field}_label'] = self.fields[f'{cliente_field}_label']
            for key, value in self.fields.items():
                if key != f'{cliente_field}_label':
                    new_fields[key] = value
            self.fields = new_fields
        else:
            # Se for criação, usar Select2
            self.fields[cliente_field].widget = ClienteSelectWidget(
                attrs={'data-placeholder': 'Selecione um cliente...', 'style': 'width: 100%;'}
            )

        # Estilização dos outros campos
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs.update({'class': 'form-check-input'})
            elif isinstance(field.widget, (forms.DateTimeInput, forms.DateInput)):
                field.widget.attrs.update({'class': 'form-control', 'type': 'datetime-local'})
            elif isinstance(field.widget, (forms.Textarea, forms.TextInput, forms.NumberInput, forms.Select)):
                field.widget.attrs.update({'class': 'form-control'})
