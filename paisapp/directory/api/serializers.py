from rest_framework import serializers

from paisapp.directory.models import Categoria, Tipo


class CategoriaSerializer(serializers.ModelSerializer[Categoria]):
    class Meta:
        model = Categoria
        fields = ["name"]

class TipoSerializer(serializers.ModelSerializer[Tipo]):
    class Meta:
        model = Tipo
        fields = ["name", "categoria"]
        # extra_kwargs = {
        #     "Categoria": {"view_name": "api:categoria-detail", "lookup_field": "pk"},
        # }
        