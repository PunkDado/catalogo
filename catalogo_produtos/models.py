#coding:utf-8
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse # Para possibilitar a manipulação de dados com forms


# Create your models here.

class Produtos(models.Model):
    nome = models.CharField(max_length=40)
    descricao = models.CharField(max_length=200)
    preco = models.FloatField()
    texto_mkt = models.CharField(max_length=200)


