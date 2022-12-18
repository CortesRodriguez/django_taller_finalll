from django.contrib import admin
from seminarioApp.models import Inscrito
# Register your models here.

class InscritoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'telefono', 'fecha', 'institucion', 'hora', 'estado', 'observacion']

admin.site.register(Inscrito, InscritoAdmin)
