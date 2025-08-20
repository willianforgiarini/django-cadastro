from django.contrib.gis.db import models


class Logradouro(models.Model):
    id = models.BigAutoField(primary_key=True)
    hierar_via = models.TextField(blank=True, null=True)
    codigo = models.CharField(blank=True, null=True)
    drenagem = models.TextField(blank=True, null=True)
    rede_eletrica = models.TextField(blank=True, null=True)
    ext_eix = models.FloatField(blank=True, null=True)
    ext_of = models.TextField(blank=True, null=True)
    gab_plan = models.FloatField(blank=True, null=True)
    gab_tot = models.TextField(blank=True, null=True)
    iluminacao = models.TextField(blank=True, null=True)
    lei_of = models.TextField(blank=True, null=True)
    nome = models.TextField(blank=True, null=True)
    obs = models.TextField(blank=True, null=True)
    pavimentacao_1 = models.TextField(blank=True, null=True)
    tipo_logr = models.TextField(blank=True, null=True)
    geom = models.LineStringField(srid=4326, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logradouro'