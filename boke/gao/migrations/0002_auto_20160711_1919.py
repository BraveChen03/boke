# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gao', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': '\u6587\u7ae0', 'verbose_name_plural': '\u6587\u7ae0'},
        ),
        migrations.AlterField(
            model_name='article',
            name='tag',
            field=models.ManyToManyField(to='gao.Tag', validators=b'\xe6\xa0\x87\xe7\xad\xbe'),
        ),
    ]
