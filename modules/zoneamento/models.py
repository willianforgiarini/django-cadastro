from django.contrib.gis.db import models


class Zoneamento(models.Model):
    geom = models.PolygonField(srid=4326, blank=True, null=True)
    zona_id = models.IntegerField(blank=True, null=True)
    macrozona = models.CharField(blank=True, null=True)
    zona = models.CharField(blank=True, null=True)
    objetivo = models.CharField(blank=True, null=True)
    local_bairro = models.CharField(blank=True, null=True)
    microzoneamento = models.CharField(blank=True, null=True)
    cau = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zoneamento'