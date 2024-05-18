from django.db import models

class Estoque(models.Model):
    nome = models.CharField(max_length=100)
    marca = models.CharField(max_length=50)
    quantidade = models.IntegerField()
    precounid = models.FloatField()

    def __str__(self):
        return self.nome
