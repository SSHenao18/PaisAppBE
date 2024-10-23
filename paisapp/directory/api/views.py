from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.mixins import UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from paisapp.directory.models import Categoria, Tipo

from .serializers import CategoriaSerializer, TipoSerializer


class CategoriaViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = CategoriaSerializer
    queryset = Categoria.objects.all()
    lookup_field = "pk"

    def get_queryset(self, *args, **kwargs):
        return self.queryset.all()
    
    def create(self, request):
        serializer = CategoriaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED, data=serializer.data)

class TipoViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = TipoSerializer
    queryset = Tipo.objects.all()
    lookup_field = "pk"

    def get_queryset(self):
        # cat_id = self.request.GET.get('id', 0)
        # if cat_id == 0:
        #     return self.queryset.all()
        # return self.queryset.filter(categoria=cat_id)
        return self.queryset.all()

    def create(self, request):
        serializer = TipoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED, data=serializer.data)