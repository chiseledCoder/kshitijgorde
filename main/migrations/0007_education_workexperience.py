# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-12 16:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20180111_2111'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=100)),
                ('degree', models.CharField(max_length=100)),
                ('school_location', models.CharField(max_length=100)),
                ('year_to_year', models.CharField(max_length=50)),
                ('last_year', models.DateField(verbose_name='Date')),
                ('currently_studying', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employer', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('company_location', models.CharField(max_length=100)),
                ('year_to_year', models.CharField(max_length=50)),
                ('last_year', models.DateField(verbose_name='Date')),
                ('currently_working', models.BooleanField(default=False)),
            ],
        ),
    ]
