from rest_framework_gis.serializers import GeometryField
from rest_framework import serializers
from django.contrib.gis.geos import (
    Polygon,
    Point
)


class PolygonSerializer(serializers.Serializer):
    geom = GeometryField()

    def validate_geom(self, value):
        if not isinstance(value, Polygon):
            raise serializers.ValidationError("A geometria deve ser do tipo Polygon.")
        return value
    

class PointSerializer(serializers.Serializer):
    point = GeometryField()

    def validate_point(self, value):
        if not isinstance(value, Point):
            raise serializers.ValidationError("A geometria deve ser do tipo Point")
        return value
