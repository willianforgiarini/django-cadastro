from rest_framework import serializers
from .models import Zoneamento


class ZoneamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zoneamento
        fields = "__all__"


class UtilizacaoSerializer(serializers.Serializer):
    utilizacao_terreno = serializers.CharField()
    count = serializers.IntegerField()


class ZoneamentoUtilizacaoSerializer(serializers.Serializer):
    zona = serializers.CharField()
    utilizacoes = UtilizacaoSerializer(many=True)