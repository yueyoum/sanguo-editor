# -*- coding: utf-8 -*-

from django.db import models

class NameFirst(models.Model):
    id = models.IntegerField(primary_key=True)
    first = models.CharField(max_length=16)

    class Meta:
        db_table = 'name_first'
        ordering = ('id',)


class NameSecond(models.Model):
    id = models.IntegerField(primary_key=True)
    second = models.CharField(max_length=255)

    class Meta:
        db_table = 'name_second'
        ordering = ('id',)



# 小秘书说话
class SecretarySpeechType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=32)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'client_secretary_speech_type'
        ordering = ('id',)
        verbose_name = '小秘书说话类型'
        verbose_name_plural = '小秘书说话类型'


class SecretarySpeech(models.Model):
    id = models.IntegerField(primary_key=True)
    content = models.CharField(max_length=255)
    tp = models.ForeignKey(SecretarySpeechType, db_column='type')
    param = models.IntegerField(default=0)

    class Meta:
        db_table = 'client_secretary_speech'
        ordering = ('id',)
        verbose_name = '小秘书说话'
        verbose_name_plural = '小秘书说话'




class GlobalString(models.Model):
    id = models.IntegerField(primary_key=True)
    enum = models.CharField(max_length=45)
    ss = models.CharField(max_length=45, db_column='str')
    desc = models.CharField(max_length=45)

    class Meta:
        db_table = 'client_global_string'
        ordering = ('id',)
        verbose_name = '全局字符串'
        verbose_name_plural = '全局字符串'


class GlobalInteger(models.Model):
    id = models.IntegerField(primary_key=True)
    enum_desc = models.CharField(max_length=255)
    value = models.IntegerField(default=0)
    desc = models.CharField(max_length=255)

    class Meta:
        db_table = 'client_global_integer'
        ordering = ('id',)
        verbose_name = '全局整数'
        verbose_name_plural = '全局整数'

