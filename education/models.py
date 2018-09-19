from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Education(models.Model):
    university = models.CharField(max_length=200, verbose_name="Universidad")
    career = models.CharField(max_length=200, verbose_name="Carrera")
    start = models.DateField(verbose_name="Fecha de inicio")
    end = models.DateField(verbose_name="Fecha de término")
    created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now = True, verbose_name="Fecha de edición")

    @property
    def startMonthAndYear(self):
        return self.start.strftime('%b, %Y')
     
    def endMonthAndYear(self):
        return self.end.strftime('%b, %Y')

    class Meta:
        verbose_name = "Educación"
        verbose_name_plural = "Educaciones"
        ordering = ['-created']
        
    def __str__(self):
        return self.university

