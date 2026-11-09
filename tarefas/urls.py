from django.urls import include, path 
from rest_framework.routers import DefaultRouter
from .views import CategoriaViewSet, TarefaViewSet


router = DefaultRouter()
router.register("categorias", CategoriaViewSet)
router.register("tarefas", TarefaViewSet)

urlpatterns = [
    path("", include(router.urls)),
]