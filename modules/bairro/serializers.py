from rest_framework import serializers
from .models import Bairro

from modules.edificacao.serializers import EdificacaoSerializer


class BairroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bairro
        fields = "__all__"


class EdificacoesPorBairro(serializers.Serializer):
    bairro = serializers.CharField()
    edificacoes = EdificacaoSerializer(many=True)