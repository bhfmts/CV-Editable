from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Award(models.Model):
    awardName = models.CharField(max_length=200, verbose_name="Premio o Certificación")
    created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now = True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Premio"
        verbose_name_plural = "Premios o Certificaciones"
        ordering = ['-created']
        
    def __str__(self):
        return self.awardName

