from django.db import models

# Create your models here.
class Auto(models.Model):
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    año = models.IntegerField()
    kilometros = models.PositiveIntegerField()
    
    def __str__(self):
        return f"{self.marca} {self.modelo}"