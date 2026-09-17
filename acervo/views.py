from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Livro
from .forms import LivroForm, BuscaForm

def inicio(request):
    return HttpResponse('Olá, acervo!')

def lista_livros(request):
    livros = Livro.objects.all()
    busca = BuscaForm(request.GET)

    if busca.is_valid():
        titulo = busca.cleaned_data['titulo']
        tipo = busca.cleaned_data['tipo']
        categoria = busca.cleaned_data['categoria']

        if titulo:
             livros = livros.filter(
                Q(titulo__icontains=titulo) | Q(autor__icontains=titulo)
            )
        if tipo:
            livros = livros.filter(tipo=tipo)
        if categoria:
            livros = livros.filter(categoria=categoria)

    return render(
        request, 'acervo/lista.html',
        {'livros': livros, 'busca': busca}
    )


def novo_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista')
    else:
        form = LivroForm()
    return render(request, 'acervo/form.html', {'form': form})
