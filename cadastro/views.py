from django.shortcuts import render, redirect
from .models import Pessoa
from .forms import PessoaForm

def index(request):
    pessoas = Pessoa.objects.all()
    contexto = {
        'pessoas': pessoas,
    }
    return render(request, 'cadastro/index.html', contexto)

def contato(request):
    return render(request, 'cadastro/contato.html')

def adicionar(request):
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PessoaForm()
    return render(request, 'cadastro/adicionar.html', {'form': form})