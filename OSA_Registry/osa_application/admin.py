from django.contrib import admin
from django.template.response import TemplateResponse
from django.urls import path

from .models import Patient,Firma, Vorscreening, Masken, Gerät,Schlafbetreuender_Arzt,DiagnosePSG,CPAP_Einstellung,CPAP_Kontrolle,Spontanous,Therapieabbruch, Medikament

admin.site.site_header='Osa_Registry'

class ObjectAdmin(admin.ModelAdmin):
    ordering = ['-order']

admin.site.register(Patient)
admin.site.register(Firma)
admin.site.register(Vorscreening)
admin.site.register(Masken)
admin.site.register(Gerät)
admin.site.register(Schlafbetreuender_Arzt)
admin.site.register(DiagnosePSG)
admin.site.register(CPAP_Einstellung)
admin.site.register(CPAP_Kontrolle)
admin.site.register(Spontanous)
admin.site.register(Therapieabbruch)
admin.site.register(Medikament)





