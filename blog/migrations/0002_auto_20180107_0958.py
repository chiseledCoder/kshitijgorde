# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-07 04:28
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
