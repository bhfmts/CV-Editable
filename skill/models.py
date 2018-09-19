from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Skill(models.Model):
    skillName = models.CharField(max_length=200, verbose_name="Habilidad")
    created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now = True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Habilidad"
        verbose_name_plural = "Habilidades"
        ordering = ['-created']
        
    def __str__(self):
        return self.skillName

