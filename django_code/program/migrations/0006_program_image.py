# Generated by Django 1.11.18 on 2019-02-21 01:18
from __future__ import unicode_literals

from django.db import migrations, models
import program.models


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0005_program_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='image',
            field=models.ImageField(default='program_thumbnails/nophoto.png', storage=program.models.OverwriteStorage(), upload_to=program.models.get_image_path),
        ),
    ]
