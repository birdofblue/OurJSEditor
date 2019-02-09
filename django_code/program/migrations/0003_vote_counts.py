# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-04-01 22:06
from __future__ import unicode_literals

from django.db import migrations, models

def count_votes(apps, schema_editor):
    # We get the model from the versioned app registry
    Program = apps.get_model("program", "Program")
    Vote = apps.get_model("vote", "Vote")

    vote_types = ["artistic", "entertaining", "informative"];

    for program in Program.objects.all():
        for t in vote_types:
            setattr(program, t + "_votes", Vote.objects.filter(vote_type=t, voted_object_id=program.program_id).count())

        program.save()

def remove_votes(apps, schema_editor):
    pass

class Migration(migrations.Migration):

    dependencies = [
        ('program', '0002_program_created'),
        ('vote', '0001_initial')
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='artistic_votes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='program',
            name='entertaining_votes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='program',
            name='informative_votes',
            field=models.IntegerField(default=0),
        ),
        migrations.RunPython(
            code=count_votes,
            reverse_code=remove_votes,
        )
    ]
