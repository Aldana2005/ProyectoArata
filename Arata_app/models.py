from django.db import models    

class Semilla(models.Model):
    variedad = models.CharField(max_length=100)
    origen = models.CharField(max_length=100)
    caracteristicas = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    estado = models.BooleanField(default=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad_disponible = models.IntegerField()
    foto = models.ImageField(upload_to='semilla_photos/', null=True, blank=True)

    def __str__(self):
        return self.variedad


