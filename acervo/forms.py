from django import forms
from .models import Livro

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo', 'autor', 'ano', 'tipo', 'categoria']

class BuscaForm(forms.Form):
    titulo = forms.CharField(label='Título ou autor', required=False)
    tipo = forms.ChoiceField(
        label='Tipo', required=False,
        choices=[('', 'Todos')] + Livro.Tipo.choices,
    )
    categoria = forms.ChoiceField(
        label='Categoria', required=False,
        choices=[('', 'Todas')] + Livro.Categoria.choices,
    )