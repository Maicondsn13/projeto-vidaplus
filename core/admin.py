from django.contrib import admin

from core.models import Paciente


# Register your models here.
@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    pass