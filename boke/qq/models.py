#coding:utf8
from django.db import models
from  gao.models import User
# Create your models here.

class QQGroup(models.Model):
    groupname = models.CharField('组名',max_length=40)
    members = models.ManyToManyField(User)
    class Meta:
        verbose_name='QQ组'
        verbose_name_plural=verbose_name
        ordering=['id']
    def __unicode__(self):
        return self.groupname
