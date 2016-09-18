# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=55)),
                ('description', models.TextField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Collector',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=55)),
                ('surname', models.CharField(max_length=55)),
                ('date_of_birth', models.DateField(verbose_name=b'date published')),
                ('email', models.EmailField(max_length=75)),
                ('phone', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=55, null=True, blank=True)),
                ('skype', models.CharField(max_length=55, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Exhibition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=55)),
                ('date', models.DateTimeField(verbose_name=b'date published')),
                ('short_description', models.CharField(max_length=255)),
                ('description', models.TextField(null=True, blank=True)),
                ('collection', models.ManyToManyField(to='exhibition.Collection')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='collection',
            name='collector',
            field=models.ForeignKey(to='exhibition.Collector'),
            preserve_default=True,
        ),
    ]
