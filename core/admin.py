from django.contrib import admin
# Colocar el modelo project en el panel de administración
from .models import Experience
# Register your models here.

class ExperienceAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated') # tupla para definir campos de solo lecture
    list_display = ("title", "company", "startMonthAndYear", "endMonthAndYear","description", "start", "end")


# Para poder registrar proyectos
admin.site.register(Experience, ExperienceAdmin)