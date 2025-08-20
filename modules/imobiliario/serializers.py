from rest_framework import serializers

from .models import (
    Imobiliario,
    ImobiliarioPessoa,
    ImobiliarioEdificacao
)


class ImobiliarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imobiliario
        fields = "__all__"


class ImobiliarioPessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImobiliarioPessoa
        fields = "__all__"


class ImobiliarioEdificacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImobiliarioEdificacao
        fields = "__all__"
    