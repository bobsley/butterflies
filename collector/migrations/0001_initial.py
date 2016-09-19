# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collector',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=55, verbose_name='\u0418\u043c\u044f')),
                ('surname', models.CharField(max_length=55, verbose_name='\u0424\u0430\u043c\u0438\u043b\u0438\u044f')),
                ('date_of_birth', models.DateField(verbose_name='\u0414\u0435\u043d\u044c \u0420\u043e\u0436\u0434\u0435\u043d\u0438\u044f')),
                ('email', models.EmailField(max_length=75, verbose_name=b'Email')),
                ('phone', models.CharField(max_length=15, verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d')),
                ('address', models.CharField(max_length=55, null=True, verbose_name='\u0410\u0434\u0440\u0435\u0441', blank=True)),
                ('skype', models.CharField(max_length=55, null=True, verbose_name=b'Skype', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
