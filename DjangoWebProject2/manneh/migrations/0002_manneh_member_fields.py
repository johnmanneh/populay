# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-07-08 06:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manneh', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='manneh',
            name='member_fields',
            field=models.CharField(choices=[('father', 'John'), ('mother', 'Sarah'), ('baby', 'Emmanuel')], default='null', max_length=30),
        ),
    ]
