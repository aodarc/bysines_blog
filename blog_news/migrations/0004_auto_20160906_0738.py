# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-06 07:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_news', '0003_auto_20160906_0736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='description',
            field=models.CharField(max_length=255, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='news',
            name='description_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='news',
            name='description_pl',
            field=models.CharField(max_length=255, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='news',
            name='description_uk',
            field=models.CharField(max_length=255, null=True, verbose_name='Description'),
        ),
    ]
