from django.db import models

class usuarios(models.Model):
    nome = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )
    codigo = models.IntegerField(
        default=0,
        null=False,
        blank=False
    )
    email = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )

    def _str_(self):
        return self.usu_name

class tarefas(models.Model):
    codigo = models.IntegerField(
        default=0,
        null=False,
        blank=False
    )
    descricao = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )
    setor = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )
    prioridade = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )
    status = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )
    data = models.DateField()

    codigo = models.ForeignKey(
        usuarios,
        on_delete=models.CASCADE
    )

tarefa = models.Manager()