# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('list_of_butterflies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listofbutterflies',
            name='name',
            field=models.CharField(help_text='name', max_length=24),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='listofbutterflies',
            name='pub_date',
            field=models.DateTimeField(null=True, verbose_name=b'date published', blank=True),
            preserve_default=True,
        ),
    ]
