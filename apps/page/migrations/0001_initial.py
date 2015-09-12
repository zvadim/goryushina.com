# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('menuitem_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='menu.MenuItem')),
                ('title', models.CharField(max_length=128)),
                ('text', models.CharField(verbose_name='Text')),
                ('slug', models.SlugField()),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('category', models.ForeignKey(blank=True, to='category.Category', null=True)),
            ],
            options={
                'ordering': ('title',),
            },
            bases=('menu.menuitem',),
        ),
    ]
