# Generated by Django 1.11.2 on 2017-08-18 16:53
from __future__ import unicode_literals

from django.db import migrations, models
from user_profile.models import generate_id


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0004_add_profile_ids_1'),
    ]

    operations = [
        # 3, change it so this is a) the primary key, b) default is generate_id
        migrations.AlterField(
            model_name='profile',
            name='profile_id',
            field=models.CharField(primary_key=True, default=generate_id, max_length=6, serialize=False),
        ),
        # 4, remove the old id field. Django defaults are lame
        migrations.RemoveField(
            model_name='profile',
            name='id',
        ),
    ]
