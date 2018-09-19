from django.contrib import admin
# Colocar el modelo project en el panel de administración
from .models import Interest
# Register your models here.

class InterestAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated') # tupla para definir campos de solo lecture


# Para poder registrar proyectos
admin.site.register(Interest, InterestAdmin)