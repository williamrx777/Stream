from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Stream)
class StreamAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nome', 'url')

@admin.register(Cdz)
class CdzAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nome', 'url')