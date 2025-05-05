from django import forms
from ..modelsDir.apolices_geral import ApolicesGerais


class ApolicesGeralForm(forms.ModelForm):
    class Meta:
        model = ApolicesGerais
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            existing_classes = field.widget.attrs.get('class', '')
            field.widget.attrs['class'] = f'{existing_classes} form-control'