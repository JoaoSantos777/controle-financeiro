from django.db import models

class Testemunha(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)

    def __str__(self):
        return self.nome
