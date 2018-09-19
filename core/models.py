from django.db import models
from django.contrib.auth.models import User
#from django.utils.dates import MONTHS
#import datetime

# Create your models here.
#Para mostra sólo años
# YEAR_CHOICES = []
# for r in range(1980, (datetime.datetime.now().year+1)):
#     YEAR_CHOICES.append((r,r))
#Para mostrar solo meses
# MONTHS_CHOICES = []
# for r in range(12, (datetime.datetime.now().month+1)):
#     MONTHS_CHOICES.append((r,r))


class Experience(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    company = models.CharField(max_length=200, verbose_name="Empresa")
    description = models.TextField(max_length=500, verbose_name="Descripción")
    start = models.DateField(verbose_name="Fecha de inicio")
    end = models.DateField(verbose_name="Fecha de término")
    #month = models.PositiveSmallIntegerField(choices=MONTHS.items())
    #year = models.IntegerField(choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now = True, verbose_name="Fecha de edición")

    

    @property
    def startMonthAndYear(self):
        return self.start.strftime('%b, %Y')
     
    def endMonthAndYear(self):
        return self.end.strftime('%b, %Y')

    class Meta:
        verbose_name = "Experiencia"
        verbose_name_plural = "Experiencias"
        ordering = ['-created']
        
    def __str__(self):
        return self.title

    
