from rest_framework import viewsets
from .models import Categoria, Tarefa
from .serializers import CategoriaSerializer, TarefaSerializer


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all().order_by("id")
    serializer_class = CategoriaSerializer


class TarefaViewSet(viewsets.ModelViewSet):
    queryset = Tarefa.objects.all().order_by("id")
    serializer_class = TarefaSerializer
