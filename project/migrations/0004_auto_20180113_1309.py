# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-13 18:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_project_project_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='featured_image',
            field=models.ImageField(default='projects/images/default.jpg', upload_to='projects/images/featured_image/'),
        ),
        migrations.AlterField(
            model_name='projectimage',
            name='image',
            field=models.ImageField(default='projects/images/default.jpg', upload_to='projects/images/associated_images'),
        ),
    ]
