from django.db import models

# Create your models here.

class Roles(models.TextChoices):
    ARRENDATARIO = 'Arrendatario','Arrendatario'
    ARRENDADOR = 'Arrendador', 'Arrendador'

class TipoInmueble(models.TextChoices):
    CASA = 'Casa','Casa'
    DEPTO = 'Depto', 'Depto'
    PARCELA = 'Parcela', 'Parcela'

class Usuario(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    rut = models.CharField(max_length=15, primary_key=True)
    direccion = models.CharField(max_length=100)
    fono = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    rol_usuario = models.CharField(max_length=15, choices=Roles.choices, default=Roles.ARRENDADOR)
    eliminado = models.BooleanField(default=False)

class Inmueble(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion= models.TextField()
    direccion = models.CharField(max_length=200)
    comuna = models.CharField(max_length=50)
    mts_cuadrados = models.IntegerField()
    mts_totales = models.IntegerField()
    precio_mensual = models.IntegerField()
    cant_estacionamientos = models.IntegerField()
    cant_habitaciones = models.IntegerField()
    cant_banos = models.IntegerField()
    disponible = models.BooleanField(default=True)
    eliminado = models.BooleanField(default=False)
    arrendatorio = models.ForeignKey(Usuario,related_name='inmuebles_arrendados', on_delete=models.CASCADE, null=True, blank=True)
    arrendador = models.ForeignKey(Usuario,related_name='inmuebles_en_arriendo',on_delete=models.CASCADE)
    