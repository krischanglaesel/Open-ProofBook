# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib.auth.views import login, logout

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^open_proofbook/', include('open_proofbook.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^accounts/login/',  login),
    (r'^accounts/logout/', logout),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
    {'document_root': settings.STATIC_DOC_ROOT}),
    (r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url': '/static/favicon.ico'}),
)

urlpatterns += patterns('proofbook.views',
    (r'^$', 'home'),
    (r'create_album/', 'create_album'),
    (r'(?P<album>[\w_]+)/(?P<curr_page>\d+)', 'album'),
    (r'(?P<album>[\w_]+)/', 'album_front',),
    (r'(?P<album>[\w_]+)/edit', 'album_edit'),
    (r'(?P<album>[\w_]+)/all', 'album_all'),
)