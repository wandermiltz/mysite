# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models

class Status(models.Model):
    code = models.IntegerField('Код')
    status = models.CharField('Статус', primary_key=True, max_length=24, )

    def __str__(self):
        return self.status

    class Meta:
        managed = True
        db_table = 'status'


class Pcb(models.Model):
    code = models.IntegerField('Код', primary_key=True)
    pcb_name = models.CharField('Название платы', max_length=64)
    customer = models.CharField('Заказчик', max_length=64)
    revision_code = models.IntegerField('Код ревизии', blank=True, null=True)
    pcb_code = models.IntegerField('Код платы', blank=True, null=True)
    #status = models.CharField('Статус', max_length=24)
    status = models.ForeignKey(Status, models.DO_NOTHING, db_column='status', blank=True, null=True)
    quantity = models.IntegerField('Количество', blank=True, null=True)

    def __str__(self):
        return self.pcb_name


    class Meta:
        managed = True
        db_table = 'pcb'
