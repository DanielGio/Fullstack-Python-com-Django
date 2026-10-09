from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Pessoa
from cadastro.forms import PessoaForm

def index(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'cadastro/index.html', {'pessoas': pessoas})

def contato(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mensagem enviada com sucesso!')
            return redirect('contato')
    else:
        form = ContatoForm()
    return render(request, 'cadastro/contato.html', {'form': form})

@login_required
def adicionar(request):
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PessoaForm()
    return render(request, 'cadastro/adicionar.html', {'form': form})

@login_required
def detalhes(request, id):
    pessoa = get_object_or_404(Pessoa, id=id)
    return render(request, 'cadastro/detalhes.html', {'pessoa': pessoa})

@login_required
def editar(request, id):
    pessoa = get_object_or_404(Pessoa, id=id)
    if request.method == 'POST':
        form = PessoaForm(request.POST, instance=pessoa)
        if form.is_valid():
            form.save()
            return redirect('detalhes', id=id)
    else:
        form = PessoaForm(instance=pessoa)
    return render(request, 'cadastro/editar.html', {'form': form, 'pessoa': pessoa})

@login_required
def deletar(request, id):
    pessoa = get_object_or_404(Pessoa, id=id)
    if request.method == 'POST':
        pessoa.delete()
        return redirect('index')
    return render(request, 'cadastro/deletar.html', {'pessoa': pessoa})