from django.contrib import admin
from .models import Page

#Configuración extra
class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('create_at','update_at')
    search_fields = ('title','content')
    list_filter = ('visible',)
    list_display = ('title', 'visible', 'create_at')
    ordering = ('create_at',)

# Register your models here.
admin.site.register(Page,PageAdmin)

# Configuración del panel de Admministración de Django
title ="Proyecto con Django"
subtitulo = "Panel de gestión"

admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = subtitulo
