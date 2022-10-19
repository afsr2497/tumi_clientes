from django.utils import timezone
from django.db import models

# Create your models here.
class pruebaClientes(models.Model):
    nombreCliente = models.CharField(max_length=30,default='')
    fechaOperacion = models.DateField(default=timezone.now)
    rosbag = models.FileField(upload_to='media/')
    videoCliente = models.FileField(upload_to='media/')
    informeCliente = models.FileField(upload_to='media/')
    resultadoCliente = models.FileField(upload_to='media/')

class ejemploArchivo(models.Model):
    nombre = models.CharField(max_length=30,default='')
    archivoImg = models.FileField(upload_to='media/')
