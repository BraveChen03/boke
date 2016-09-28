# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gao', '0002_auto_20160711_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='pid',
            field=models.ForeignKey(verbose_name=b'\xe7\x88\xb6\xe7\xba\xa7\xe8\xaf\x84\xe8\xae\xba', blank=True, to='gao.Comment', null=True),
        ),
    ]
