# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='page',
            name='category',
            field=models.ForeignKey(blank=True, to='category.Category', null=True),
        ),
    ]
