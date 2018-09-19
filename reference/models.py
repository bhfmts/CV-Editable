from django.db import models

# Create your models here.
class Reference(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    apellido = models.CharField(max_length=100, default="", verbose_name="Apellido")
    cargo = models.CharField(max_length=100, verbose_name="Cargo")
    empresa = models.CharField(max_length=2000,verbose_name="Nombre empresa")
    celular = models.CharField(max_length=50, verbose_name="Teléfono")
    email = models.EmailField(verbose_name="E-mail")
    created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now = True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Referencia"
        verbose_name_plural = "Referencias"
        
        
    def __str__(self):
        return self.nombre
