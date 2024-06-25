from django.db import models


# Create your models here.

class Moto(models.Model):
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    año = models.IntegerField()
    kilometros = models.PositiveIntegerField()
    imagen = models.ImageField(upload_to='motos', blank=True,null=True)
    
    def __str__(self):
        return f"{self.marca} {self.modelo}"
    
