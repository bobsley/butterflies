# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exhibition', '0002_auto_20160917_1054'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='type_collection',
            field=models.CharField(max_length=55, null=True, blank=True),
            preserve_default=True,
        ),
    ]
