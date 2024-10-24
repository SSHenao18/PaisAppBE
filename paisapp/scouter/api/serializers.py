from rest_framework import serializers

from paisapp.scouter.models import Scout

class ScoutSerializer(serializers.ModelSerializer[Scout]):
    class Meta:
        model = Scout
        fields = ["name", "img", "latitude", "longitude", "created_at"]