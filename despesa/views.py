from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

import despesa
from .models import Despesa
from .forms import FiltroDespesaForm
from politico.models import Politico
from django.urls import reverse_lazy
from django.db.models import Sum
from .forms import DespesaForm


# Despesa 
class DespesaListView(ListView):
    model = Despesa
    template_name = 'despesa_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['soma_despesas'] = Despesa.objects.aggregate(total=Sum('valor'))['total'] or 0
        return context

class DespesaCreateView(CreateView):
    model = Despesa
    template_name = 'despesa_form.html'
    form_class = DespesaForm
    success_url = reverse_lazy('despesa-list')

    def form_valid(self, form):
        # Atualiza o valor disponível da renda quando a despesa for registrada
        renda_utilizada = form.cleaned_data['renda_utilizada']
        valor_despesa = form.cleaned_data['valor']

        if renda_utilizada:
            renda_utilizada.atualizar_valor_disponivel(valor_despesa)

        return super().form_valid(form)


class DespesaUpdateView(UpdateView):
    model = Despesa
    template_name = 'despesa_form.html'
    fields = ['nome', 'categoria', 'valor', 'data', 'descricao', 'renda_utilizada']
    success_url = reverse_lazy('despesa-list')


class DespesaDeleteView(DeleteView):
    model = Despesa
    template_name = 'despesa_confirm_delete.html'
    success_url = reverse_lazy('despesa-list')

def politico_detalhe(request, pk):
    politico = get_object_or_404(Politico, pk=pk)
    despesa = Despesa.objects.filter(politico=politico)

    if request.method == 'GET':
        form = FiltroDespesaForm(request.GET)
        if form.is_valid():
            categoria = form.cleaned_data['categoria']
            if categoria:
                despesa = despesa.filter(categoria=categoria)
    else:
        form = FiltroDespesaForm()

    return render(request, 'politico_detalhe.html', {
        'politico': politico,
        'despesa': despesa,
        'form': form
    })