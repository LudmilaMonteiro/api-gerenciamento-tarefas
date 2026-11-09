from django.db.models.deletion import ProtectedError
from rest_framework import status, viewsets
from rest_framework.response import Response

from .models import Categoria, Tarefa
from .serializers import CategoriaSerializer, TarefaSerializer


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all().order_by("id")
    serializer_class = CategoriaSerializer

    def destroy(self, request, *args, **kwargs):
        categoria = self.get_object()

        try:
            categoria.delete()
        except ProtectedError:
            return Response(
                {
                    "erro": "Não é possível excluir uma categoria que possui tarefas."
                },
                status=status.HTTP_409_CONFLICT
            )

        return Response(status=status.HTTP_204_NO_CONTENT)


class TarefaViewSet(viewsets.ModelViewSet):
    queryset = Tarefa.objects.all().order_by("id")
    serializer_class = TarefaSerializer
