from django.contrib.gis.db import models


class Bairro(models.Model):
    codigo = models.IntegerField(blank=True, null=True)
    nome = models.CharField(blank=True, null=True)
    geom = models.PolygonField(srid=4326, blank=True, null=True)
    cau = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bairro'