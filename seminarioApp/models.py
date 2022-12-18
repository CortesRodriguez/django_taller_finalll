from django.db import models
opcion = estado = [
 [0, "Reservado"],
 [1,"Completado"],
 [2,"Anulado"],
 [3,"No Asisten"]
]
# Create your models here.
class Inscrito(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField()
    fecha = models.DateField()
    institucion = models.CharField(max_length=50)
    hora = models.TimeField()
    estado = models.IntegerField(choices= opcion)
    observacion = models.CharField(max_length=100, blank=True)

