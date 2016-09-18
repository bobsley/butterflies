# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exhibition', '0004_remove_collection_type_collection'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='description',
            field=models.TextField(null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='collection',
            name='name',
            field=models.CharField(max_length=55, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043a\u043e\u043b\u043b\u0435\u043a\u0446\u0438\u0438'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='exhibition',
            name='date',
            field=models.DateTimeField(verbose_name='\u0414\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f \u043f\u0440\u043e\u0432\u0435\u0434\u0435\u043d\u0438\u044f'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='exhibition',
            name='description',
            field=models.TextField(null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='exhibition',
            name='name',
            field=models.CharField(max_length=55, verbose_name='\u041d\u0430\u0437\u0432\u043d\u0438\u0435 \u0432\u044b\u0441\u0442\u0430\u0432\u043a\u0438'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='exhibition',
            name='short_description',
            field=models.CharField(max_length=255, verbose_name='\u041a\u0440\u0430\u0442\u043a\u043e\u0435 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435'),
            preserve_default=True,
        ),
    ]
