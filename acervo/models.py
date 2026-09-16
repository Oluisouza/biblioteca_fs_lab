from django.db import models

class Livro(models.Model):

    class Tipo(models.TextChoices):
        FISICO = 'fisico', 'Físico'
        DIGITAL = 'digital', 'Digital'

    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    ano = models.IntegerField()
    disponivel = models.BooleanField(default=True)
    tipo = models.CharField(max_length=7, choices=Tipo.choices, default=Tipo.FISICO)

    def __str__(self):
        return self.titulo