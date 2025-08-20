from django.contrib.gis.db import models


class Pessoa(models.Model):
    codigo = models.CharField(blank=True, null=True)
    nome = models.CharField(blank=True, null=True)
    cpf_cnpj = models.CharField(blank=True, null=True)
    proprietario_cep = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pessoa'