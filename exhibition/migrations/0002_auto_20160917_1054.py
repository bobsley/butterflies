# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exhibition', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collector',
            name='address',
            field=models.CharField(max_length=55, null=True, verbose_name='\u0410\u0434\u0440\u0435\u0441', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='collector',
            name='date_of_birth',
            field=models.DateField(verbose_name='\u0414\u0435\u043d\u044c \u0420\u043e\u0436\u0434\u0435\u043d\u0438\u044f'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='collector',
            name='email',
            field=models.EmailField(max_length=75, verbose_name=b'Email'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='collector',
            name='name',
            field=models.CharField(max_length=55, verbose_name='\u0418\u043c\u044f'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='collector',
            name='phone',
            field=models.CharField(max_length=15, verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='collector',
            name='skype',
            field=models.CharField(max_length=55, null=True, verbose_name=b'Skype', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='collector',
            name='surname',
            field=models.CharField(max_length=55, verbose_name='\u0424\u0430\u043c\u0438\u043b\u0438\u044f'),
            preserve_default=True,
        ),
    ]
