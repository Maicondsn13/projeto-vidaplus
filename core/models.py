from django.db import models

# Create your models here.

from django.db import models


class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.nome


class Profissional(models.Model):
    nome = models.CharField(max_length=100)
    especialidade = models.CharField(max_length=100)
    crm = models.CharField(max_length=20)

    def __str__(self):
        return self.nome


class Unidade(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.TextField()

    def __str__(self):
        return self.nome


class Consulta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE)
    unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE)
    data_hora = models.DateTimeField()

    def __str__(self):
        return f"Consulta de {self.paciente.nome} com {self.profissional.nome}"


class Prontuario(models.Model):
    consulta = models.OneToOneField(Consulta, on_delete=models.CASCADE)
    descricao = models.TextField()
    prescricao = models.TextField()

    def __str__(self):
        return f"Prontuário da consulta {self.consulta.id}"
