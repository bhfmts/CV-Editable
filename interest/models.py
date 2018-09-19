from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Interest(models.Model):
    interest = models.TextField(max_length=1000, verbose_name="Describe tu interés")
    created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now = True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Interés"
        verbose_name_plural = "Intereses"
        ordering = ['-created']
        
    def __str__(self):
        return self.interest

