from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Renda
from django.db.models import Sum

class RendaListView(ListView):
    model = Renda
    template_name = 'renda_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['soma_rendas'] = Renda.objects.aggregate(total=Sum('valor'))['total'] or 0
        return context

class RendaCreateView(CreateView):
    model = Renda
    template_name = 'renda_form.html'
    fields = ['nome', 'categoria', 'valor', 'valor_disponivel', 'data_recebimento']
    success_url = reverse_lazy('renda-list')

class RendaUpdateView(UpdateView):
    model = Renda
    template_name = 'renda_form.html'
    fields = ['nome', 'categoria', 'valor', 'valor_disponivel', 'data_recebimento']
    success_url = reverse_lazy('renda-list')

class RendaDeleteView(DeleteView):
    model = Renda
    template_name = 'renda_confirm_delete.html'
    success_url = reverse_lazy('renda-list')
