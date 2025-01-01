from django.db import models

class Eleitor(models.Model):
    nome = models.CharField(max_length=100)
    rg = models.CharField(max_length=15, unique=True)
    cpf = models.CharField(max_length=11, unique=True)
    rua = models.CharField(max_length=150)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=100)
    cep = models.CharField(max_length=8)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)  # Abreviação do estado (ex: 'SP')
    banco = models.CharField(max_length=50)
    chave_pix = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
