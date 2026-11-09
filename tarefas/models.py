from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome

class Tarefa(models.Model):
    STATUS_CHOICES = [
        ("pendente", "Pendente"),
        ("andamento", "Em andamento"),
        ("concluida", "Concluída"),
    ]

    titulo = models.CharField(max_length=150)
    descricao = models.TextField(blank=True)
    prazo = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pendente")
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name="tarefas")

    def __str__(self):
        return self.titulo
