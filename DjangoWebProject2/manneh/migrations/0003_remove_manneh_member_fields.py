# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-07-08 06:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manneh', '0002_manneh_member_fields'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manneh',
            name='member_fields',
        ),
    ]