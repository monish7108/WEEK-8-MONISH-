# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-21 10:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usingmodels', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='personal_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'personal_details',
            },
        ),
    ]