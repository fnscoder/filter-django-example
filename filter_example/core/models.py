from django.db import models

class Especialidade(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.nome


class Medico(models.Model):
    nome = models.CharField(max_length=20)
    crm = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    telefone = models.CharField(max_length=11)
    especialidade = models.ForeignKey(Especialidade, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.nome
