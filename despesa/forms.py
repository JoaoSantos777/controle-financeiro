from django import forms
from categoria_despesa.models import CategoriaDespesa

class FiltroDespesaForm(forms.Form):
    categoria = forms.ModelChoiceField(
        queryset=CategoriaDespesa.objects.all(),
        empty_label='Selecione uma categoria',
        required=False
    )
