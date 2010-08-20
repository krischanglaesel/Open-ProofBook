# -*- coding: utf-8 -*-
from django.contrib import admin
from open_proofbook.proofbook.models import Album, Site, Category

admin.site.register(Album)
admin.site.register(Site)
admin.site.register(Category)