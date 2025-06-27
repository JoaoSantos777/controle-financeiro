from django import forms
from .models import Despesa
from categoria_despesa.models import CategoriaDespesa
from renda.models import Renda

class FiltroDespesaForm(forms.Form):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')  # pega o user da view
        super().__init__(*args, **kwargs)
        self.fields['categoria'].queryset = CategoriaDespesa.objects.filter(user=user)

    categoria = forms.ModelChoiceField(
        queryset=CategoriaDespesa.objects.none(),  
        empty_label='Selecione uma categoria',
        required=False
    )

class DespesaForm(forms.ModelForm):
    class Meta:
        model = Despesa
        fields = ['nome', 'categoria', 'valor', 'data', 'descricao', 'renda_utilizada']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')  # pega o user da view
        super().__init__(*args, **kwargs)
        self.fields['categoria'].queryset = CategoriaDespesa.objects.filter(user=user)
        self.fields['renda_utilizada'].queryset = Renda.objects.filter(user=user)

    def clean(self):
        cleaned_data = super().clean()
        valor_despesa = cleaned_data.get('valor')
        renda_utilizada = cleaned_data.get('renda_utilizada')

        if renda_utilizada and valor_despesa > renda_utilizada.valor_disponivel:
            raise forms.ValidationError("Saldo insuficiente na renda selecionada para cobrir esta despesa.")

        return cleaned_data
