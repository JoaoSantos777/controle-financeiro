from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Renda
from .forms import RendaForm
from django.db.models import Sum

class RendaListView(ListView):
    model = Renda
    template_name = 'renda_list.html'

    def get_queryset(self):
        return Renda.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['soma_rendas'] = self.get_queryset().aggregate(total=Sum('valor'))['total'] or 0
        return context

class RendaCreateView(CreateView):
    model = Renda
    template_name = 'renda_form.html'
    form_class = RendaForm
    success_url = reverse_lazy('renda-list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user  # passa usuário para o form
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class RendaUpdateView(UpdateView):
    model = Renda
    template_name = 'renda_form.html'
    form_class = RendaForm
    success_url = reverse_lazy('renda-list')

    def get_queryset(self):
        return Renda.objects.filter(user=self.request.user)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

class RendaDeleteView(DeleteView):
    model = Renda
    template_name = 'renda_confirm_delete.html'
    success_url = reverse_lazy('renda-list')

    def get_queryset(self):
        return Renda.objects.filter(user=self.request.user)
