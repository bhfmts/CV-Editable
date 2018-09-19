from django.contrib import admin
from .models import About
# Register your models here.

class AboutAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated') # tupla para definir campos de solo lecture


# Para poder registrar proyectos
admin.site.register(About, AboutAdmin)
# Register your models here.
