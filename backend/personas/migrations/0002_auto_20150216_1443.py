# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='foto',
            field=models.ImageField(upload_to=b'personas/img'),
            preserve_default=True,
        ),
    ]
