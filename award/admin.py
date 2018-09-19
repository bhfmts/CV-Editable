from django.contrib import admin
# Colocar el modelo project en el panel de administración
from .models import Award
# Register your models here.

class AwardAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated') # tupla para definir campos de solo lecture


# Para poder registrar proyectos
admin.site.register(Award, AwardAdmin)