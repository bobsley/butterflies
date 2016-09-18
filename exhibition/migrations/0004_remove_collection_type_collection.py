# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exhibition', '0003_collection_type_collection'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collection',
            name='type_collection',
        ),
    ]
