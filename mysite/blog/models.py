from django.db import models

# Create your models here.

from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

def publish(self):
    self.published_date = timezone.now()
    self.save()

def __str__(self):
    return self.title

class Persona (models.Model):
    nombre_completo = models.CharField(max_length=60)
    rut = models.CharField(max_length=11)
    email = models.EmailField()
    fecha_nac = models.DateField()
    telefono = models.IntegerField()
    region = models.CharField(max_length=30)
    comuna = models.CharField(max_length=30)
    casa = models.CharField(max_length=15)

class Mascota(models.Model):
    nombre = models.CharField(max_length=50)
    raza = models.CharField(max_length=50)
    descripcion= models.CharField(max_length=100)
    estado = models.CharField(max_length=15)
    fotografia = models.ImageField()