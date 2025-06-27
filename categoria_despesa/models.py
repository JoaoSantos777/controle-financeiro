from django.db import models
from django.contrib.auth.models import User

class CategoriaDespesa(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome