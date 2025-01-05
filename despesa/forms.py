from django import forms
from .models import Despesa
from categoria_despesa.models import CategoriaDespesa

class FiltroDespesaForm(forms.Form):
    categoria = forms.ModelChoiceField(
        queryset=CategoriaDespesa.objects.all(),
        empty_label='Selecione uma categoria',
        required=False
    )

class DespesaForm(forms.ModelForm):
    class Meta:
        model = Despesa
        fields = ['nome', 'categoria', 'valor', 'data', 'descricao', 'renda_utilizada']

    def clean(self):
        cleaned_data = super().clean()
        valor_despesa = cleaned_data.get('valor')
        renda_utilizada = cleaned_data.get('renda_utilizada')

        if renda_utilizada and valor_despesa > renda_utilizada.valor_disponivel:
            raise forms.ValidationError("Saldo insuficiente na renda selecionada para cobrir esta despesa.")

        return cleaned_data
