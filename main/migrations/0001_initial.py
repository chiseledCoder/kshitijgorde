# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-15 20:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutMe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('display_pic', models.ImageField(default='profile/default.png', upload_to='profile/')),
                ('tagline', models.CharField(default='', max_length=100)),
                ('dob', models.DateField(verbose_name='Date')),
                ('address', models.TextField(default='')),
                ('nationality', models.CharField(default='Indian', max_length=50)),
                ('email', models.EmailField(default='', max_length=254)),
                ('phone', models.IntegerField(default='91 9096081092')),
            ],
        ),
    ]
