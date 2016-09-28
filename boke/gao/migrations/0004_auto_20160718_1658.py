# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('gao', '0003_auto_20160713_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='friend',
            field=models.ManyToManyField(related_name='friend_rel_+', null=True, verbose_name='\u670b\u53cb', to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.AlterField(
            model_name='ad',
            name='callback_url',
            field=models.URLField(max_length=255, verbose_name='\u5e7f\u544a\u8fde\u63a5', blank=True),
        ),
        migrations.AlterField(
            model_name='ad',
            name='date_publish',
            field=models.DateTimeField(auto_now_add=True, verbose_name='\u6dfb\u52a0\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='ad',
            name='desc',
            field=models.TextField(max_length=100, verbose_name='\u5e7f\u544a\u7b80\u4ecb', blank=True),
        ),
        migrations.AlterField(
            model_name='ad',
            name='image_url',
            field=models.ImageField(default='upload/default.jpg', upload_to='ad/%Y/%m', verbose_name='\u56fe\u7247\u5730\u5740'),
        ),
        migrations.AlterField(
            model_name='ad',
            name='index',
            field=models.IntegerField(default=999, verbose_name='\u4ece\u5c0f\u5230\u5927\u6392\u5e8f'),
        ),
        migrations.AlterField(
            model_name='ad',
            name='title',
            field=models.CharField(max_length=30, verbose_name='\u6807\u9898'),
        ),
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ForeignKey(verbose_name='\u6587\u7ae0\u5206\u7c7b', to='gao.Category'),
        ),
        migrations.AlterField(
            model_name='article',
            name='click_count',
            field=models.IntegerField(default=0, verbose_name='\u70b9\u51fb\u91cf'),
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(verbose_name='\u5185\u5bb9'),
        ),
        migrations.AlterField(
            model_name='article',
            name='date_publish',
            field=models.DateTimeField(auto_now_add=True, verbose_name='\u6dfb\u52a0\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='article',
            name='desc',
            field=models.CharField(max_length=100, verbose_name='\u7b80\u4ecb'),
        ),
        migrations.AlterField(
            model_name='article',
            name='is_recommend',
            field=models.BooleanField(default=False, verbose_name='\u662f\u5426\u63a8\u8350'),
        ),
        migrations.AlterField(
            model_name='article',
            name='tag',
            field=models.ManyToManyField(to='gao.Tag', verbose_name='\u6807\u7b7e'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=30, verbose_name='\u6807\u9898'),
        ),
        migrations.AlterField(
            model_name='article',
            name='user',
            field=models.ForeignKey(verbose_name='\u7528\u6237', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='category',
            name='index',
            field=models.IntegerField(default=999, verbose_name='\u4ece\u5c0f\u5230\u5927\u6392\u5217'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=30, verbose_name='\u540d\u5b57'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='article',
            field=models.ForeignKey(verbose_name='\u6587\u7ae0', to='gao.Article'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(verbose_name='\u8bc4\u8bba\u5185\u5bb9'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date_publish',
            field=models.DateTimeField(auto_now_add=True, verbose_name='\u8bc4\u8bba\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='pid',
            field=models.ForeignKey(verbose_name='\u7236\u7ea7\u8bc4\u8bba', blank=True, to='gao.Comment', null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(verbose_name='\u7528\u6237', blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='links',
            name='callback_url',
            field=models.URLField(max_length=255, verbose_name='\u94fe\u63a5\u5730\u5740', blank=True),
        ),
        migrations.AlterField(
            model_name='links',
            name='date_publish',
            field=models.DateTimeField(auto_now_add=True, verbose_name='\u6dfb\u52a0\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='links',
            name='desc',
            field=models.TextField(max_length=100, verbose_name='\u94fe\u63a5\u7b80\u4ecb'),
        ),
        migrations.AlterField(
            model_name='links',
            name='index',
            field=models.IntegerField(default=999, verbose_name='\u4ece\u5c0f\u5230\u5927\u6392\u5e8f'),
        ),
        migrations.AlterField(
            model_name='links',
            name='title',
            field=models.CharField(max_length=30, verbose_name='\u94fe\u63a5\u6807\u9898'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=50, verbose_name='\u6807\u7b7e\u5b57'),
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='upload/default.jpg', upload_to='avatar/%Y/%m', verbose_name='\u5934\u50cf'),
        ),
        migrations.AlterField(
            model_name='user',
            name='nick',
            field=models.CharField(max_length=30, verbose_name='\u6635\u79f0', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=23, verbose_name='\u7535\u8bdd', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='url',
            field=models.URLField(max_length=30, verbose_name='\u4e2a\u4eba\u4e3b\u9875', blank=True),
        ),
    ]
