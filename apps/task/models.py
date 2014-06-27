# -*- coding:utf-8 -*-

from django.db import models


class Task(models.Model):
    id = models.IntegerField(primary_key=True)
    tp = models.IntegerField("类型")
    func = models.ForeignKey('config.FunctionDefine', null=True, blank=True, verbose_name='对应功能')
    name = models.CharField("名字", max_length=32)
    first = models.BooleanField("初始任务", default=False)
    times = models.IntegerField("次数")
    sycee = models.IntegerField("奖励元宝", null=True, blank=True)
    gold = models.IntegerField("奖励金币", null=True, blank=True)
    next_task = models.IntegerField("下一档任务ID", null=True, blank=True)
    link = models.CharField("链接", max_length=255, blank=True)

    class Meta:
        db_table = 'task'
        ordering = ('id',)
        verbose_name = "日常任务"
        verbose_name_plural = "日常任务"
