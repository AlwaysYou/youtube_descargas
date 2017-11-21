# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from filebrowser.sites import site
from ckeditor_uploader import urls as ck_urls
from apps.web import urls as web_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^ckeditor/', include(ck_urls)),
    url(r'', include(web_urls, namespace='web')),
    # url(r'^localeurl/', include('localeurl.urls')),

    # url(r'', include(web_urls, namespace='web')),
] + (static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) +
     static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))


handler404 = 'apps.web.views.page_404'
handler500 = 'apps.web.views.page_500'
