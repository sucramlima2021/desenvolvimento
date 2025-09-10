from django import forms
from ..modelsDir.sinistros import Sinistros
from ..modelsDir.apolices_geral import ApoliceBase


    
class DateInput(forms.DateInput):
    input_type = "date"

class SinistrosForm(forms.ModelForm):
    class Meta:
        model = Sinistros
        fields = [
            "apolice", "titular",
            "premio", "Is", "iea_diag", "ipa_aux", "ifptd", "valor",
            "data", "tipo", "observacoes",
            "tipo_morte", "data_obito", "data_com_vg", "data_com_cia",
            "data_recusa_pg",
            "nome_segurado", "cpf_segurado", "status"
        ]
        widgets = {
            "data": DateInput(),
            "data_obito": DateInput(),
            "data_com_vg": DateInput(),
            "data_com_cia": DateInput(),
            "data_recusa_pg": DateInput(),
            "observacoes": forms.Textarea(attrs={"rows": 3}),
            
        
            
        }
        
        help_texts = {
            "pago_recusa": "Marque quando houver pagamento ou recusa consolidada.",
        }

    def __init__(self, *args, **kwargs):
        cliente = kwargs.pop('cliente', None)
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            existing_classes = field.widget.attrs.get('class', '')
            if not isinstance(field.widget, forms.RadioSelect) and not isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = f'{existing_classes} form-control form-control-sm'
        if cliente:
            self.fields['apolice'].queryset = ApoliceBase.objects.filter(cliente=cliente)