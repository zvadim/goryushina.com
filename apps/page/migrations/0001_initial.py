# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '__first__'),
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
                'verbose_name_plural': 'Categories',
            },
            bases=('menu.menuitem',),
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('menuitem_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='menu.MenuItem')),
                ('title', models.CharField(max_length=128)),
                ('text', tinymce.models.HTMLField(help_text=b'The best video/photo size is 695x390', verbose_name='Text')),
                ('slug', models.SlugField()),
                ('preview', sorl.thumbnail.fields.ImageField(upload_to=b'page_preview')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('category', models.ForeignKey(blank=True, to='page.Category', null=True)),
            ],
            options={
                'ordering': ('title',),
            },
            bases=('menu.menuitem',),
        ),
    ]
