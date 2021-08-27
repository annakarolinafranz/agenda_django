from django.db import models
from django.utils import timezone

class Categoria(models.Model):
    nome = models.CharField(max_length=55)

    def __str__(self):
        return self.nome


class Contato(models.Model):
    nome = models.CharField(max_length=55)
    sobrenome = models.CharField(max_length=55, blank=True)
    telefone = models.CharField(max_length=55)
    email = models.CharField(max_length=55, blank=True)
    data_criacao = models.DateTimeField(default=timezone.now)
    descricao = models.TextField(blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    mostrar = models.BooleanField(default=True)  # boolean mostra verdadeiro ou falso, default já deixa ativado como verdadeiro
    foto = models.ImageField(blank=True, upload_to='foto/%Y/%m/%d')

    def __str__(self):
        return self.nome

