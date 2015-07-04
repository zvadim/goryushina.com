# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_auto_20150704_1105'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menu',
            options={'ordering': ('order',)},
        ),
        migrations.AlterField(
            model_name='menu',
            name='order',
            field=models.IntegerField(default=999, editable=False),
        ),
    ]
