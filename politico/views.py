from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Politico
from .forms import PoliticoForm
from despesa.models import Despesa
from despesa.forms import FiltroDespesaForm



def test_view(request):
    return HttpResponse("This is a test view.")

# Politico
class PoliticoListView(ListView):
    model = Politico
    template_name = 'politico_list.html'
    context_object_name = 'politico'

    def get_queryset(self):
        return Politico.objects.all()



class PoliticoCreateView(CreateView):
    model = Politico
    form_class = PoliticoForm
    template_name = 'politico_form.html'
    success_url = reverse_lazy('politico-list')


    
class PoliticoUpdateView(UpdateView):
    model = Politico
    template_name = 'politico_form.html'
    fields = ['nome', 'cpf', 'cnpj', 'partido', 'cargo', 'email', 'telefone', 'data_nascimento']
    success_url = reverse_lazy('politico-list')


class PoliticoDeleteView(DeleteView):
    model = Politico
    template_name = 'politico_confirm_delete.html'
    success_url = reverse_lazy('politico-list')


def politico_detalhe(request, pk):
    politico = get_object_or_404(Politico, pk=pk)
    despesa = Despesa.objects.filter(politico=politico)

    form = FiltroDespesaForm(request.GET)
    if form.is_valid():
        categoria = form.cleaned_data['categoria']
        if categoria:
            despesa = despesa.filter(categoria=categoria)
    
    return render(request, 'politico_detalhe.html', {
        'politico': politico,
        'despesa': despesa,
        'form': form
    })
