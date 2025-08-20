from django.contrib.gis.db import models

from modules.setor.models import Setor


class Quadra(models.Model):
    geom = models.PolygonField(srid=4326, blank=True, null=True)
    cod = models.CharField(max_length=20, blank=True, null=True)
    area = models.DecimalField(max_digits=65535, decimal_places=2, blank=True, null=True)
    perimetro = models.DecimalField(max_digits=65535, decimal_places=2, blank=True, null=True)
    id_setor = models.ForeignKey(Setor, models.DO_NOTHING, db_column='id_setor', blank=True, null=True)
    quadra = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'quadra'
