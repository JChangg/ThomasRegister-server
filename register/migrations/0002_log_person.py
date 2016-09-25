# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-25 15:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('register', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Person'),
        ),
    ]
