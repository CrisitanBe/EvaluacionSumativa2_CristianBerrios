from django.contrib import admin
from .models import Cliente,Atencion


# Register your models here.

admin.register(Cliente)
class ClineteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'mascota')
    list_editable = ('sintomas')
    list_per_page = 25

admin.register(Atencion)
class AtencionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'mascota')
    list_editable = ('sintomas',)
    list_per_page = 25



@admin.register(Cliente)
class ClineteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'mascota')

@admin.register(Atencion)
class AtencionAdmin(admin.ModelAdmin):
    list_display = ('asistencia','pabellon')