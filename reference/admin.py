from django.contrib import admin
from .models import Reference
# Register your models here.

class ReferenceAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated') # tupla para definir campos de solo lecture


# Para poder registrar proyectos
admin.site.register(Reference, ReferenceAdmin)
# Register your models here.
