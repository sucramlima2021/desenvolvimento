from django import forms
from ..modelsDir.sinistros import Sinistros
from django_select2.forms import ModelSelect2Widget
from ..modelsDir.clientes import Clientes

class ClienteSelectWidget(ModelSelect2Widget):
    model = Clientes
    search_fields = ['nome__icontains', 'cpf__icontains']

    def label_from_instance(self, obj):
        return f'{obj.nome} - {obj.cpf}'
    
class DateInput(forms.DateInput):
    input_type = "date"

class SinistrosForm(forms.ModelForm):
    class Meta:
        model = Sinistros
        fields = [
            "cliente", "apolice", "titular",
            "premio", "Is", "iea_diag", "ipa_aux", "ifptd", "valor",
            "data", "tipo", "observacoes",
            "tipo_morte", "data_obito", "data_com_vg", "data_com_cia",
            "pago_recusa", "data_recusa_pg",
            "nome_segurado", "cpf_segurado",
        ]
        widgets = {
            "data": DateInput(),
            "data_obito": DateInput(),
            "data_com_vg": DateInput(),
            "data_com_cia": DateInput(),
            "data_recusa_pg": DateInput(),
            "observacoes": forms.Textarea(attrs={"rows": 3}),
            'cliente': ClienteSelectWidget(attrs={'data-placeholder':'Selecione um Cliente...', 'style':'width:100%', 'data-minimum-input-length': 0},)
        }
        help_texts = {
            "pago_recusa": "Marque quando houver pagamento ou recusa consolidada.",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            existing_classes = field.widget.attrs.get('class', '')
            if not isinstance(field.widget, forms.RadioSelect):
                field.widget.attrs['class'] = f'{existing_classes} form-control form-control-sm'