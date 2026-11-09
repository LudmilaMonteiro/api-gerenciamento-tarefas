
from datetime import timedelta

from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Categoria, Tarefa


class TarefaAPITests(APITestCase):

    def setUp(self):
        self.categoria = Categoria.objects.create(
            nome="Estudos",
            descricao="Tarefas acadêmicas"
        )

        self.tarefa = Tarefa.objects.create(
            titulo="Estudar Django",
            descricao="Aprender Django REST Framework",
            prazo=timezone.localdate() + timedelta(days=7),
            status="pendente",
            categoria=self.categoria
        )

    def test_cadastrar_tarefa(self):
        dados = {
            "titulo": "Fazer atividade",
            "descricao": "Atividade de manutenção",
            "prazo": str(timezone.localdate() + timedelta(days=5)),
            "status": "pendente",
            "categoria": self.categoria.id
        }

        resposta = self.client.post("/api/tarefas/", dados)

        self.assertEqual(resposta.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Tarefa.objects.count(), 2)

    def test_consultar_tarefa(self):
        resposta = self.client.get(
            f"/api/tarefas/{self.tarefa.id}/"
        )

        self.assertEqual(resposta.status_code, status.HTTP_200_OK)
        self.assertEqual(resposta.data["titulo"], "Estudar Django")

    def test_atualizar_tarefa(self):
        resposta = self.client.patch(
            f"/api/tarefas/{self.tarefa.id}/",
            {"status": "andamento"}
        )

        self.assertEqual(resposta.status_code, status.HTTP_200_OK)

        self.tarefa.refresh_from_db()
        self.assertEqual(self.tarefa.status, "andamento")

    def test_excluir_tarefa(self):
        resposta = self.client.delete(
            f"/api/tarefas/{self.tarefa.id}/"
        )

        self.assertEqual(resposta.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(
            Tarefa.objects.filter(id=self.tarefa.id).exists()
        )

    def test_prazo_invalido(self):
        dados = {
            "titulo": "Tarefa atrasada",
            "descricao": "Teste de validação",
            "prazo": str(timezone.localdate() - timedelta(days=1)),
            "status": "pendente",
            "categoria": self.categoria.id
        }

        resposta = self.client.post("/api/tarefas/", dados)

        self.assertEqual(resposta.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("prazo", resposta.data)
        self.assertEqual(Tarefa.objects.count(), 1)
