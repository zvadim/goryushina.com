# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields
import apps.gallery.models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='file',
            field=sorl.thumbnail.fields.ImageField(height_field=b'height', width_field=b'width', upload_to=apps.gallery.models.get_path),
        ),
        migrations.AlterField(
            model_name='image',
            name='page',
            field=models.ForeignKey(related_name='gallery', to='page.Page'),
        ),
    ]
