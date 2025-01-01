from django.db import models

class Renda(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Renda")
    categoria = models.ForeignKey('categoria_renda.CategoriaRenda', on_delete=models.SET_NULL, null=True) 
    valor = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor")
    data_recebimento = models.DateField(verbose_name="Data de Recebimento")

    def __str__(self):
        return f"{self.nome} - R$ {self.valor}"
