# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exhibition', '0005_auto_20160918_0909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='collector',
            field=models.ForeignKey(verbose_name='\u041a\u043e\u043b\u043b\u0435\u043a\u0446\u0438\u043e\u043d\u0435\u0440', to='exhibition.Collector'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='exhibition',
            name='collection',
            field=models.ManyToManyField(to='exhibition.Collection', verbose_name='\u041a\u043e\u043b\u043b\u0435\u043a\u0446\u0438\u0438'),
            preserve_default=True,
        ),
    ]
