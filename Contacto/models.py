from django.db import models

# Create your models here.

class Contacto(models.Model):
    nombre = models.CharField(max_length=30)
    email = models.EmailField()
    asunto = models.CharField(max_length=100)
    mensaje = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.nombre} {self.asunto} {self.mensaje} {self.fecha_envio}"
