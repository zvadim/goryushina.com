# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps.gallery.models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('file', models.ImageField(height_field=b'height', width_field=b'width', upload_to=apps.gallery.models.get_path)),
                ('width', models.IntegerField(editable=False)),
                ('height', models.IntegerField(editable=False)),
                ('create_dt', models.DateTimeField(auto_now_add=True)),
                ('edit_dt', models.DateTimeField(auto_now=True)),
                ('page', models.ForeignKey(to='page.Page')),
            ],
        ),
    ]
