# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-11-20 22:40
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import filebrowser.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banners',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pestana', models.CharField(choices=[('SO', 'SOMOS'), ('CLI', 'CLIENTES'), ('TES', 'TESTIMONIOS'), ('CO', 'CONTACTO'), ('SE', 'SERVICIOS')], default='SO', max_length=30, verbose_name='Pestaña')),
                ('titulo', models.CharField(max_length=200, verbose_name='Título')),
                ('fondo', filebrowser.fields.FileBrowseField(blank=True, help_text='Tamaño Recomendado: 1080x132', max_length=200, verbose_name='Fondo:')),
            ],
            options={
                'verbose_name_plural': 'Banners',
                'verbose_name': 'Banners',
            },
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=200, verbose_name='Nombres')),
                ('apellido', models.CharField(blank=True, max_length=200, verbose_name='Apellidos')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Email')),
                ('telefono', models.CharField(blank=True, max_length=20, verbose_name='Teléfono')),
                ('fecha', models.DateField(auto_now_add=True, verbose_name='Fecha')),
                ('servicio', models.CharField(blank=True, max_length=200, verbose_name='Tipo de servicio')),
            ],
            options={
                'verbose_name_plural': 'Contactos',
                'verbose_name': 'Contacto',
            },
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.SmallIntegerField(default=0, verbose_name='Posición')),
                ('direccion', models.CharField(max_length=300, verbose_name='Email')),
            ],
            options={
                'verbose_name_plural': 'ubicaciones',
                'verbose_name': 'ubicacion',
            },
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.SmallIntegerField(default=0, verbose_name='Posición')),
                ('email', models.CharField(max_length=120, verbose_name='Email')),
            ],
            options={
                'verbose_name_plural': 'Emails',
                'verbose_name': 'Email',
            },
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo_servicios', models.CharField(blank=True, max_length=100, verbose_name='Título servicios')),
                ('titulo_somos', models.CharField(blank=True, max_length=100, verbose_name='Título somos')),
                ('texto_somos', ckeditor.fields.RichTextField(blank=True, verbose_name='Texto somos')),
                ('img_somos', filebrowser.fields.FileBrowseField(blank=True, help_text='Tamaño Recomendado: 585x410', max_length=200, verbose_name='Imagen')),
                ('boton_somos', models.CharField(blank=True, max_length=300, verbose_name='Título boton somos')),
                ('titulo_clientes', models.CharField(blank=True, max_length=300, verbose_name='Título clientes')),
                ('boton_clientes', models.CharField(blank=True, max_length=300, verbose_name='Texto boton clientes')),
            ],
            options={
                'verbose_name_plural': 'Home',
                'verbose_name': 'Home',
            },
        ),
        migrations.CreateModel(
            name='HomeBanner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.SmallIntegerField(default=0, verbose_name='Posición')),
                ('texto', models.CharField(blank=True, max_length=100, verbose_name='Texto')),
                ('texto_boton', models.CharField(blank=True, max_length=100, null=True, verbose_name='Texto de botón')),
                ('enlace_boton', models.CharField(blank=True, max_length=100, verbose_name='Enlace del botón')),
                ('imagen', filebrowser.fields.FileBrowseField(help_text='Tamaño Recomendado: 1920x570', max_length=200, verbose_name='Imagen:')),
            ],
            options={
                'ordering': ['position'],
                'verbose_name_plural': 'Banners de Home',
                'verbose_name': 'Banner de Home',
            },
        ),
        migrations.CreateModel(
            name='InfoSite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True, verbose_name='Activo')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('created_by', models.IntegerField(default=0, editable=False, null=True, verbose_name='Creado por')),
                ('modified_by', models.IntegerField(default=0, editable=False, null=True, verbose_name='Modificado por')),
                ('email_form', models.CharField(blank=True, help_text='Separar correos con comas', max_length=200, verbose_name='Email de Formulario de Contacto')),
                ('twitter', models.URLField(blank=True, verbose_name='Twitter')),
                ('facebook', models.URLField(blank=True, verbose_name='Facebook')),
                ('site', models.CharField(blank=True, help_text='Ingrese la url actual del sitio sin el slash final', max_length=60, verbose_name='URL del sitio')),
                ('ga', models.CharField(blank=True, help_text='Opcional: Inserte el código que google analitycs le\n       proporciona con el formato: UA-XXXXX-X', max_length=24, verbose_name='Google Analytics')),
            ],
            options={
                'verbose_name_plural': 'Información del Sitio',
            },
        ),
        migrations.CreateModel(
            name='SeccionCliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', ckeditor.fields.RichTextField(blank=True, verbose_name='Texto')),
                ('boton', models.CharField(blank=True, max_length=100, verbose_name='Texto botón')),
                ('enlace', models.CharField(blank=True, max_length=300, verbose_name='Enlace boton')),
            ],
            options={
                'verbose_name_plural': 'Sección clientes',
                'verbose_name': 'Sección clientes',
            },
        ),
        migrations.CreateModel(
            name='SeccionContacto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(blank=True, max_length=200, verbose_name='Título')),
                ('texto', ckeditor.fields.RichTextField(blank=True, verbose_name='Texto')),
                ('imagen', filebrowser.fields.FileBrowseField(blank=True, help_text='Tamaño recomendado:160x45', max_length=200, verbose_name='imagen')),
            ],
            options={
                'verbose_name_plural': 'Sección Contacto',
                'verbose_name': 'Sección Contacto',
            },
        ),
        migrations.CreateModel(
            name='Somos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('introduccion', ckeditor.fields.RichTextField(blank=True, verbose_name='Introduccion')),
                ('texto', ckeditor.fields.RichTextField(blank=True, verbose_name='Texto')),
                ('imagen', filebrowser.fields.FileBrowseField(blank=True, help_text='Tamaño recomendado:470x430', max_length=200, verbose_name='imagen')),
                ('boton', models.CharField(blank=True, max_length=100, verbose_name='Texto botón')),
                ('enlace', models.CharField(blank=True, max_length=200, verbose_name='Enlace botón')),
                ('texto_redes', models.CharField(blank=True, max_length=200, verbose_name='Texto redes sociales')),
            ],
            options={
                'verbose_name_plural': 'Somos',
                'verbose_name': 'Somos',
            },
        ),
        migrations.CreateModel(
            name='Telefono',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.SmallIntegerField(default=0, verbose_name='Posición')),
                ('telefono', models.CharField(blank=True, max_length=120, verbose_name='Teléfono')),
                ('info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='info_tel', to='web.InfoSite')),
            ],
            options={
                'verbose_name_plural': 'Teléfonos',
                'verbose_name': 'Teléfono',
            },
        ),
        migrations.CreateModel(
            name='Testimonio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.SmallIntegerField(default=0, verbose_name='Posición')),
                ('titulo', models.CharField(blank=True, max_length=200, verbose_name='Título')),
                ('texto', ckeditor.fields.RichTextField(blank=True, verbose_name='Texto')),
                ('autor', models.CharField(blank=True, max_length=100, verbose_name='Autor')),
                ('imagen', filebrowser.fields.FileBrowseField(help_text='Tamaño Recomendado: 128x128', max_length=200, verbose_name='Imagen:')),
                ('active', models.BooleanField(default=True, verbose_name='Mostrar')),
            ],
            options={
                'ordering': ['position'],
                'verbose_name_plural': 'Testimonios',
                'verbose_name': 'Testimonio',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.SmallIntegerField(default=0, verbose_name='Posición')),
                ('estado', models.BooleanField(default=False, verbose_name='Estado')),
                ('url', models.URLField(blank=True, null=True, verbose_name='Url')),
            ],
            options={
                'verbose_name_plural': 'Videos',
                'verbose_name': 'Video',
            },
        ),
        migrations.CreateModel(
            name='VideoTitulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(blank=True, max_length=400, null=True, verbose_name='Titulo')),
                ('fecha', models.DateField(auto_now_add=True, verbose_name='Fecha')),
            ],
            options={
                'verbose_name_plural': 'Videos',
                'verbose_name': 'Video',
            },
        ),
        migrations.AddField(
            model_name='video',
            name='video_titulo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='web.VideoTitulo'),
        ),
        migrations.AddField(
            model_name='email',
            name='info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='info_email', to='web.InfoSite'),
        ),
        migrations.AddField(
            model_name='direccion',
            name='info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='info_direccion', to='web.InfoSite'),
        ),
    ]
