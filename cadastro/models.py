from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    idade = models.IntegerField()
    telefone = models.CharField(max_length=20, blank=True)
    apelido = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.nome
    
class Contato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    assunto = models.CharField(max_length=150)
    mensagem = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)  # guarda quando foi enviado

    def __str__(self):
        return f'{self.assunto} - {self.nome}'
    
class Telefone(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, related_name='telefones')
    numero = models.CharField(max_length=20)

    def __str__(self):
        return self.numero
    