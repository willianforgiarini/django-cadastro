from django.contrib.gis.db import models


class Edificacao(models.Model):
    inscricao = models.CharField(max_length=200, blank=True, null=True)
    geom = models.PolygonField(srid=4326, blank=True, null=True)
    origem = models.BigIntegerField(blank=True, null=True)
    unidade = models.CharField(max_length=200, blank=True, null=True)
    id_lote = models.IntegerField(blank=True, null=True)
    dt_criacao = models.DateTimeField(blank=True, null=True)
    dt_atualizacao = models.DateTimeField(blank=True, null=True)
    area = models.FloatField(blank=True, null=True)
    endereco = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'edificacao'
