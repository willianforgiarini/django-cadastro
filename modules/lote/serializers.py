from rest_framework import serializers
from .models import Lote


class LoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lote
        fields = "__all__"
        