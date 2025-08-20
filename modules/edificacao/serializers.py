from rest_framework import serializers
from .models import Edificacao


class EdificacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Edificacao
        fields = "__all__"