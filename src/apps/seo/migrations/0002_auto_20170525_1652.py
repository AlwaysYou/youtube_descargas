# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-25 21:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seo',
            name='meta_description',
            field=models.CharField(blank=True, help_text='Máximo 160 caracteres', max_length=160, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='seo',
            name='meta_robots',
            field=models.CharField(blank=True, help_text='Por ejemplo: "noindex, nofollow"', max_length=60, verbose_name='Etiqueta "meta:robots"'),
        ),
        migrations.AlterField(
            model_name='seo',
            name='meta_title',
            field=models.CharField(blank=True, help_text='Máximo: 50 caracteres', max_length=50, verbose_name='Título'),
        ),
        migrations.AlterField(
            model_name='seo',
            name='og_description',
            field=models.CharField(blank=True, help_text='Máximo 300 caracteres', max_length=300, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='seo',
            name='og_title',
            field=models.CharField(blank=True, help_text='Máximo: 40 caracteres', max_length=40, verbose_name='Título'),
        ),
        migrations.AlterField(
            model_name='seo',
            name='url',
            field=models.CharField(db_index=True, help_text='Debe ingresar la url relativa. Por ejemplo: "/contacto/"', max_length=200, unique=True, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='seo',
            name='url_canonica',
            field=models.URLField(blank=True, help_text='Las urls relativas no están permitidas', verbose_name='URL Canónica'),
        ),
    ]
