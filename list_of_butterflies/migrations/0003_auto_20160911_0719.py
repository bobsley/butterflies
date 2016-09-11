# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('list_of_butterflies', '0002_auto_20160911_0700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listofbutterflies',
            name='pub_date',
            field=models.DateTimeField(verbose_name=b'date published', blank=True),
            preserve_default=True,
        ),
    ]
