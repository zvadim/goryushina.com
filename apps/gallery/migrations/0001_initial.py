# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields
import apps.gallery.models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('file', sorl.thumbnail.fields.ImageField(height_field=b'height', width_field=b'width', upload_to=apps.gallery.models.get_path)),
                ('width', models.IntegerField(editable=False)),
                ('height', models.IntegerField(editable=False)),
                ('create_dt', models.DateTimeField(auto_now_add=True)),
                ('edit_dt', models.DateTimeField(auto_now=True)),
                ('page', models.ForeignKey(related_name='gallery', to='page.Page')),
            ],
        ),
    ]
