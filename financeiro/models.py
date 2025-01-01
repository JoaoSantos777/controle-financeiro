'''from django.db import models
from django.utils import timezone

class Partido(models.Model):
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=10)

    def __str__(self):
        return self.sigla

class Politico(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    partido = models.ForeignKey(Partido, on_delete=models.CASCADE)
    cargo = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.nome


class CategoriaDespesa(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    


class Despesa(models.Model):
    politico = models.ForeignKey('Politico', on_delete=models.CASCADE)
    categoria = models.ForeignKey('CategoriaDespesa', on_delete=models.SET_NULL, null=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField(default=timezone.now)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.politico} - {self.categoria} - {self.valor}"


'''