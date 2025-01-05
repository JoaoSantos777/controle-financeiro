from django.db import models

class Renda(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Renda")
    categoria = models.ForeignKey('categoria_renda.CategoriaRenda', on_delete=models.SET_NULL, null=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor")
    valor_disponivel = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor Disponível", default=0.00)
    data_recebimento = models.DateField(verbose_name="Data de Recebimento")

    def __str__(self):
        return f"{self.nome} - R$ {self.valor}"

    def atualizar_valor_disponivel(self, valor_despesa):
        """Atualiza o valor disponível da renda após uma despesa."""
        if valor_despesa > self.valor_disponivel:
            raise ValueError("Saldo insuficiente para cobrir a despesa.")
        self.valor_disponivel -= valor_despesa
        self.save()
