from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Pessoa
from .forms import PessoaForm, ContatoForm

def index(request):
    # recebe todas as "Pessoas" do banco de dados
    pessoas = Pessoa.objects.order_by('nome')
    total = Pessoa.objects.count()

    return render(request, 'cadastro/index.html', {'pessoas': pessoas, 'total': total})

def adicionar(request):
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PessoaForm()
    return render(request, 'cadastro/adicionar.html', {'form': form})

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

def detalhes(request, id):
    pessoa = get_object_or_404(Pessoa, id=id)
    return render(request, 'cadastro/detalhes.html', {'pessoa': pessoa})

def editar(request, id):
    pessoa = get_object_or_404(Pessoa, id=id)
    if request.method == 'POST':
        form = PessoaForm(request.POST, instance=pessoa)
        if form.is_valid():
            form.save()
            return redirect('detalhes', id=pessoa.id)
    else:
        form = PessoaForm(instance=pessoa)
    return render(request, 'cadastro/adicionar.html', {'form': form})

def deletar(request, id):
    pessoa = get_object_or_404(Pessoa, id=id)
    if request.method == 'POST':
        pessoa.delete()
        return redirect('index')
    return render(request, 'cadastro/deletar.html', {'pessoa': pessoa})