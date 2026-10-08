from django import forms
from .models import Pessoa, Contato


class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'


class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'assunto', 'mensagem']