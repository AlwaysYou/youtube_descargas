# -*- coding: utf-8 -*-
# Stdlib imports

# Core django imports
from django.conf import settings
from django.contrib import admin
# Third party app imports
from singlemodeladmin import SingleModelAdmin
from filebrowser.settings import ADMIN_THUMBNAIL
from apps.core.actions import export_as_csv_action
from .models import (Home, HomeBanner, Testimonio,
                     Banners, InfoSite, Telefono, Email,
                     Direccion, Contacto, SeccionContacto,
                     Somos,
                     Video,
                     VideoTitulo)
from pytube import YouTube
from apps.web.models.utils import printProgressBar
from time import sleep


@admin.register(Banners)
class BannersAdmin(admin.ModelAdmin):
    model = Banners
    list_display = ['titulo', 'miniatura', 'pestana']

    def miniatura(self, obj):
        if obj.fondo and obj.fondo.filetype == "Image":
            return u'<img src="%s" />' % obj.fondo.version_generate(
                ADMIN_THUMBNAIL).url
        else:
            return ""

    miniatura.allow_tags = True
    miniatura.short_description = u"Imagen"


@admin.register(HomeBanner)
class BannerHomeAdmin(admin.ModelAdmin):
    model = HomeBanner
    list_display = ['miniatura', 'position']
    ordering = ['position']
    list_editable = ['position']

    def miniatura(self, obj):
        if obj.imagen and obj.imagen.filetype == "Image":
            return u'<img src="%s" />' % obj.imagen.version_generate(
                ADMIN_THUMBNAIL).url
        else:
            return ""

    miniatura.allow_tags = True
    miniatura.short_description = u"Imagen"


@admin.register(Testimonio)
class TestimonioAdmin(admin.ModelAdmin):
    list_display = ['autor', 'miniatura', 'position']
    ordering = ['position']
    list_editable = ['position']

    def miniatura(self, obj):
        if obj.imagen and obj.imagen.filetype == "Image":
            return u'<img src="%s" />' % obj.imagen.version_generate(
                ADMIN_THUMBNAIL).url
        else:
            return ""

    miniatura.allow_tags = True
    miniatura.short_description = u"Imagen"


@admin.register(Home)
class HomeAdmin(SingleModelAdmin):
    pass


@admin.register(Somos)
class SomosAdmin(SingleModelAdmin):
    pass


class EmailInline(admin.StackedInline):
    model = Email
    extra = 0


class TelefonoInline(admin.StackedInline):
    model = Telefono
    extra = 0


class DireccionInline(admin.StackedInline):
    model = Direccion
    extra = 0


@admin.register(InfoSite)
class InfoSiteAdmin(SingleModelAdmin):
    fieldsets = (
        ('Información de contacto', {'fields': ('email_form', )}),
        ('Social', {'fields': ('twitter', 'facebook')}),
        ('Información del sitio', {'fields': ('site', 'ga')}),
    )
    inlines = [EmailInline, TelefonoInline, DireccionInline]

    def has_add_permission(self, request):
        info = InfoSite.objects.all()
        if info:
            return False
        else:
            return True

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    ordering = ['-fecha']
    list_display = ['nombre', 'apellido', 'telefono', 'email', 'fecha']
    search_fields = ('nombre', 'apellido', 'email', 'fecha')
    list_per_page = 25
    actions = [export_as_csv_action()]


class VideoInline(admin.StackedInline):
    model = Video
    extra = 0


@admin.register(VideoTitulo)
class VideoTituloAdmin(admin.ModelAdmin):
    list_display = 'titulo', 'fecha'
    inlines = VideoInline,
    fields = 'titulo', 'fecha',
    readonly_fields = 'fecha',
    actions = ['descargar_videos', ]

    path = '/home/daniel/pytube_downloads'

    def printProgressBar(iteration, total,
                         prefix='',
                         suffix='',
                         decimals=1,
                         length=100,
                         fill='█'):
        """
        Call in a loop to create terminal progress bar
        @params:
            iteration   - Required  : current iteration (Int)
            total       - Required  : total iterations (Int)
            prefix      - Optional  : prefix string (Str)
            suffix      - Optional  : suffix string (Str)
            decimals    - Optional  : positive number of decimals in percent complete (Int)
            length      - Optional  : character length of bar (Int)
            fill        - Optional  : bar fill character (Str)
        """
        percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
        filledLength = int(length * iteration // total)
        bar = fill * filledLength + '-' * (length - filledLength)
        print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r')
        # Print New Line on Complete
        if iteration == total: 
            print()


    def descargar_videos(self, request, queryset):
        for obj in queryset:
            todos_videos = obj.videos.all()
            items = list(range(0, 57))
            l = len(items)


            # Initial call to print 0% progress
            printProgressBar(0, l, prefix='Progress:',
                             suffix='Complete',
                             length=50)
            for i, item in enumerate(items):
                # Do stuff...
                sleep(0.1)
                # Update Progress Bar
                printProgressBar(i + 1, l, prefix='Progress:',
                                 suffix='Complete', length=50)
            for row in todos_videos:
                yt = YouTube(row.url)
                video = yt.get('mp4', '720p')
                row.estado = True
                row.save()
                video.download(self.path)


