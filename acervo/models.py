from django.db import models

class Livro(models.Model):

    class Tipo(models.TextChoices):
        FISICO = 'fisico', 'Físico'
        DIGITAL = 'digital', 'Digital'

    class Categoria(models.TextChoices):
        GENERALIDADES = '000', '000 – Generalidades e Informação'
        FILOSOFIA = '100', '100 – Filosofia e Psicologia'
        RELIGIAO = '200', '200 – Religião e Teologia'
        CIENCIAS_SOCIAIS = '300', '300 – Ciências Sociais e Direito'
        LINGUISTICA = '400', '400 – Linguística e Idiomas'
        CIENCIAS_PURAS = '500', '500 – Ciências Puras (Exatas e Naturais)'
        CIENCIAS_APLICADAS = '600', '600 – Ciências Aplicadas (Tecnologia)'
        ARTES = '700', '700 – Artes e Recreação'
        LITERATURA = '800', '800 – Literatura'
        HISTORIA = '900', '900 – História e Geografia'

    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    ano = models.IntegerField()
    disponivel = models.BooleanField(default=True)
    tipo = models.CharField(max_length=7, choices=Tipo.choices, default=Tipo.FISICO)
    categoria = models.CharField(max_length=3, choices=Categoria.choices)

    def __str__(self):
        return self.titulo