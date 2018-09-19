from django.db import models

# Create your models here.
class About(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    apellido = models.CharField(max_length=100, default="", verbose_name="Apellido")
    address = models.CharField(max_length=200, verbose_name="Dirección")
    cellphone = models.CharField(max_length=50, verbose_name="Teléfono")
    email = models.EmailField(verbose_name="E-mail")
    description = models.TextField(max_length=2000,verbose_name="Acerca de ti")
    image = models.ImageField(verbose_name="Imagen", upload_to="profile") # para subir todas las imagenes 
    created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now = True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Información personal"
        verbose_name_plural = "Datos personales"
        
        
    def __str__(self):
        return self.name
