from django.db import models

class Partido(models.Model):
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=10)

    def __str__(self):
        return self.sigla