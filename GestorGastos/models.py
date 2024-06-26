from django.db import models

# Create your models here.

from django.db import models
from django.utils import timezone


class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    contrasenia = models.CharField(max_length=128)
    saldo = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.nombre

class CategoriaGasto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nombre

class Gasto(models.Model):
    fecha = models.DateTimeField(default=timezone.now)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.CharField(max_length=255)

    categoria = models.ForeignKey(CategoriaGasto, on_delete=models.SET_NULL, null=True, blank=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='gastos')

    def __str__(self):
        return f"{self.descripcion} - {self.monto}"

class Ingreso(models.Model):
    fecha = models.DateTimeField(default=timezone.now)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fuente = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255, null=True, blank=True)

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='ingresos')

    def __str__(self):
        return f"{self.fuente} - {self.monto}"
