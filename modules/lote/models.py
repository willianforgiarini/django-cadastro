from django.contrib.gis.db import models

from modules.bairro.models import Bairro
from modules.quadra.models import Quadra


class Lote(models.Model):
    codigo_cadastro = models.CharField(blank=True, null=True)
    inscricao_cartografica = models.CharField(max_length=35, blank=True, null=True)
    tipo_cadastro = models.CharField(blank=True, null=True)
    situacao_cadastral = models.CharField(blank=True, null=True)
    area_total_construida = models.DecimalField(max_digits=65535, decimal_places=2, blank=True, null=True)
    situacao_na_quadra = models.IntegerField(blank=True, null=True)
    topografia = models.IntegerField(blank=True, null=True)
    pedologia = models.IntegerField(blank=True, null=True)
    ocupacao = models.IntegerField(blank=True, null=True)
    patrimonio_terreno = models.IntegerField(blank=True, null=True)
    murado = models.IntegerField(blank=True, null=True)
    passeio = models.IntegerField(blank=True, null=True)
    imune_isento_iptu = models.IntegerField(blank=True, null=True)
    nro_habite_se = models.CharField(blank=True, null=True)
    tipo_isencao = models.IntegerField(blank=True, null=True)
    area_terreno = models.DecimalField(max_digits=65535, decimal_places=2, blank=True, null=True)
    bciobservacao = models.CharField(blank=True, null=True)
    geom = models.PolygonField(srid=4326, blank=True, null=True)
    ct_data_alteracao = models.DateTimeField(blank=True, null=True)
    dt_criacao = models.DateTimeField(blank=True, null=True)
    dt_atualizacao = models.DateTimeField(blank=True, null=True)
    quadra = models.ForeignKey(Quadra, models.SET_NULL, db_column='id_quadra', blank=True, null=True)
    id_face_quadra = models.IntegerField(blank=True, null=True)
    bairro = models.ForeignKey(Bairro, models.SET_NULL, db_column='id_bairro', blank=True, null=True)
    utilizacao_terreno = models.IntegerField(blank=True, null=True)
    matricula = models.CharField(blank=True, null=True)
    georreferenciamento = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lote'