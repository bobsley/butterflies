# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0003_auto_20160919_1715'),
        ('collector', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=55, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043a\u043e\u043b\u043b\u0435\u043a\u0446\u0438\u0438')),
                ('description', models.TextField(null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True)),
                ('collector', models.ForeignKey(verbose_name='\u041a\u043e\u043b\u043b\u0435\u043a\u0446\u0438\u043e\u043d\u0435\u0440', blank=True, to='collector.Collector', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Exhibition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=55, verbose_name='\u041d\u0430\u0437\u0432\u043d\u0438\u0435 \u0432\u044b\u0441\u0442\u0430\u0432\u043a\u0438')),
                ('date', models.DateTimeField(verbose_name='\u0414\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f \u043f\u0440\u043e\u0432\u0435\u0434\u0435\u043d\u0438\u044f')),
                ('short_description', models.CharField(max_length=255, verbose_name='\u041a\u0440\u0430\u0442\u043a\u043e\u0435 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435')),
                ('description', models.TextField(null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True)),
                ('assistant', models.ForeignKey(related_name='assistant_exhibition', verbose_name='\u0410\u0441\u0441\u0438\u0441\u0442\u0435\u043d\u0442', blank=True, to='sponsors.Sponsor', null=True)),
                ('collection', models.ManyToManyField(to='exhibition.Collection', verbose_name='\u041a\u043e\u043b\u043b\u0435\u043a\u0446\u0438\u0438')),
                ('sponsor', models.ForeignKey(related_name='sponsor_exhibition', verbose_name='\u0421\u043f\u043e\u043d\u0441\u043e\u0440', blank=True, to='sponsors.Sponsor', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
