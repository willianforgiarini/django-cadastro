from rest_framework import serializers
from .models import Quadra


class QuadraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quadra
        fields = "__all__"


class AreaConstruidaPorQuadraSerializer(serializers.Serializer):
    quadra = serializers.IntegerField()
    codigo = serializers.CharField()
    area_construida = serializers.FloatField()