# -*- coding:utf-8 -*-

from django.db import models

class ForbiddenWord(models.Model):
    word = models.CharField(max_length=32)

    class Meta:
        db_table = 'forbidden_word'
        verbose_name = "敏感词"
        verbose_name_plural = "敏感词"
