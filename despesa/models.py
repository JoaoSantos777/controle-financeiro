from django.db import models
from django.utils import timezone
from renda.models import Renda

class Despesa(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Despesa", null=True, blank=True)
    politico = models.ForeignKey('politico.Politico', on_delete=models.CASCADE, null=True, blank=True)
    categoria = models.ForeignKey('categoria_despesa.CategoriaDespesa', on_delete=models.SET_NULL, null=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor")
    data = models.DateField(default=timezone.now)
    descricao = models.TextField(blank=True, null=True)
    renda_utilizada = models.ForeignKey(Renda, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Renda Utilizada", related_name="despesas")

    def __str__(self):
        return f"{self.politico} - {self.categoria} - {self.valor}"
    
     # Método para exibir os detalhes de uma despesa associada a uma renda
    def get_renda_utilizada(self):
        if self.renda_utilizada:
            return f"{self.renda_utilizada.nome} - R$ {self.renda_utilizada.valor}"
        return "Nenhuma renda associada"
