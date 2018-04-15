# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class InventoryTurnover(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField()

DOCUMENT_TYPE = (
        ('WZ', 'WZ'),
        ('PZ', 'PZ'),
        ('RW', 'RW'),
        ('PW', 'PW'),
        )

class Document(models.Model):
    document_type = models.CharField(max_length=2, choices=DOCUMENT_TYPE)
    number = IntegerField()
    date = models.DateTime()

    @property
    def full_number(self):
        return self.documetn_type + '/' + self.number + '/' + self.date

    def __str__(self):
        return self.number

