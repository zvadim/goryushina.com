# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('menuitem_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='menu.MenuItem')),
                ('title', models.CharField(max_length=128)),
                ('slug', models.SlugField()),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ('title',),
            },
            bases=('menu.menuitem',),
        ),
    ]
