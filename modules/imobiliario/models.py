from django.contrib.gis.db import models

from modules.lote.models import Lote
from modules.pessoa.models import Pessoa
from modules.logradouro.models import Logradouro
from modules.edificacao.models import Edificacao


class Imobiliario(models.Model):
    numero_cadastro = models.CharField(blank=True, null=True)
    inscricao_imobiliaria = models.CharField(blank=True, null=True)
    complemento = models.CharField(blank=True, null=True)
    status = models.CharField(blank=True, null=True)
    tipo_cadastro = models.CharField(blank=True, null=True)
    tipo = models.CharField(blank=True, null=True)
    alinhamento = models.CharField(blank=True, null=True)
    estado_conservacao = models.CharField(blank=True, null=True)
    locacao = models.CharField(blank=True, null=True)
    situacao = models.CharField(blank=True, null=True)
    estrutura = models.CharField(blank=True, null=True)
    cobertura = models.CharField(blank=True, null=True)
    paredes = models.CharField(blank=True, null=True)
    revestimento_externo = models.CharField(blank=True, null=True)
    vedacao_esquadrias = models.CharField(blank=True, null=True)
    patrimonio_unidade = models.CharField(blank=True, null=True)
    murado = models.CharField(blank=True, null=True)
    passeio = models.CharField(blank=True, null=True)
    ct_data_alteracao = models.DateTimeField(blank=True, null=True)
    dt_criacao = models.DateTimeField(blank=True, null=True)
    dt_atualizacao = models.DateTimeField(blank=True, null=True)
    lote = models.ForeignKey(Lote, models.SET_NULL, db_column='id_lote', blank=True, null=True)
    matricula = models.CharField(blank=True, null=True)
    area_total_construida = models.DecimalField(max_digits=65535, decimal_places=2, blank=True, null=True)
    area_terreno = models.CharField(blank=True, null=True)
    area_comum = models.CharField(blank=True, null=True)
    area_terreno_escritura = models.CharField(blank=True, null=True)
    area_construida_averbada = models.CharField(blank=True, null=True)
    geom = models.PointField(srid=4326, blank=True, null=True)
    inscricao_cartografica = models.TextField(blank=True, null=True)
    id_logradouro = models.ForeignKey(Logradouro, models.DO_NOTHING, db_column='id_logradouro', blank=True, null=True)
    nr_porta = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'imobiliario'


class ImobiliarioPessoa(models.Model):
    pessoa = models.ForeignKey(Pessoa, models.DO_NOTHING, db_column='id_pessoa', blank=True, null=True)
    imobiliario = models.ForeignKey(Imobiliario, models.DO_NOTHING, db_column='id_imobiliario', blank=True, null=True)
    proprietario_percentual = models.CharField(blank=True, null=True)
    tipo = models.CharField(blank=True, null=True)
    dt_criacao = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'imobiliario_pessoa'


class ImobiliarioEdificacao(models.Model):
    imobiliario = models.ForeignKey(Imobiliario, models.DO_NOTHING, db_column='id_imobiliario')
    edificacao = models.ForeignKey(Edificacao, models.DO_NOTHING, db_column='id_edificacao')
    dt_criacao = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'imobiliario_edificacao'
        unique_together = (('imobiliario', 'edificacao'),)