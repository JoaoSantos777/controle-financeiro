from django.db import models
from django.utils import timezone

class Despesa(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Despesa",   null=True, blank=True)
    politico = models.ForeignKey('politico.Politico', on_delete=models.CASCADE,  null=True, blank=True) 
    categoria = models.ForeignKey('categoria_despesa.CategoriaDespesa', on_delete=models.SET_NULL, null=True) 
    valor = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor")
    data = models.DateField(default=timezone.now)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.politico} - {self.categoria} - {self.valor}"
