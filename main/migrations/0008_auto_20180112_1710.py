# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-12 17:10
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_education_workexperience'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='designation',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='testimony',
            field=ckeditor.fields.RichTextField(),
        ),
    ]