# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-03-16 21:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maincat', '0002_auto_20200316_1922'),
    ]

    operations = [
        migrations.RenameField(
            model_name='maincat',
            old_name='title',
            new_name='category',
        ),
    ]
