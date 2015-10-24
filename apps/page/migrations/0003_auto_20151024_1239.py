# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0002_auto_20151010_1647'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='page',
            options={'ordering': ('order', 'title')},
        ),
        migrations.AddField(
            model_name='page',
            name='order',
            field=models.IntegerField(default=999, editable=False),
        ),
    ]
