
from django.utils import timezone
from rest_framework import serializers

from .models import Categoria, Tarefa


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ["id", "nome", "descricao"]


class TarefaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarefa
        fields = [
            "id",
            "titulo",
            "descricao",
            "prazo",
            "status",
            "categoria",
        ]

    def validate_prazo(self, value):
        if value < timezone.localdate():
            raise serializers.ValidationError(
                "O prazo não pode ser anterior à data atual."
            )
        return value
