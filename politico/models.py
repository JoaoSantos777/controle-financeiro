from django.db import models

class Politico(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    cnpj = models.CharField(max_length=14, blank=True, null=True)
    partido = models.ForeignKey('partido.Partido', on_delete=models.CASCADE)
    cargo = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.nome
