from django.contrib.gis.db import models


class Setor(models.Model):
    id = models.IntegerField(primary_key=True)
    geom = models.PolygonField(srid=4326, blank=True, null=True)
    setor = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'setor'