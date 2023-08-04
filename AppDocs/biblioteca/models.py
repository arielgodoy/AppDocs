# models.py

from django.db import models
from django.contrib.auth.models import User

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser, Group, Permission

class CustomUser(AbstractUser):
    # Agrega campos personalizados aquí si los necesitas
    groups = models.ManyToManyField(Group, related_name='custom_users')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_users')
    

# Create your models here.
class Avatar(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    imagen = models.ImageField(default='default.jpg',upload_to='avatares',null = True, blank=True)
    def __str__(self):
        return f'{self.user} {self.imagen}'
    


class TipoDocumento(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Propietario(models.Model):
    ROL_CHOICES = (
        ('persona', 'Persona Natural'),
        ('sociedad', 'Sociedad'),
    )

    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=20, unique=True)
    telefono = models.CharField(max_length=20)
    rol = models.CharField(max_length=20, choices=ROL_CHOICES)

    def __str__(self):
        return self.nombre

class Propiedad(models.Model):
    rol = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE)

    def __str__(self):
        return self.rol

class Documento(models.Model):
    TIPOS_ARCHIVO = (
        ('pdf', 'PDF'),
        ('jpeg', 'JPEG'),
        ('dwg', 'DWG'),
    )

    tipo_documento = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE)
    Nombre_documento = models.CharField(max_length=100)
    propiedad = models.ForeignKey(Propiedad, on_delete=models.CASCADE)
    archivo = models.FileField(upload_to='archivos_documentos/')

    def __str__(self):
        return f"{self.tipo_documento} - {self.propiedad.rol}"






class Conversacion(models.Model):
    participantes = models.ManyToManyField(User, related_name='conversaciones')
    def __str__(self):
        return ', '.join([str(participante) for participante in self.participantes.all()])

class Mensaje(models.Model):
    conversacion = models.ForeignKey(Conversacion, on_delete=models.CASCADE, related_name='mensajes')
    remitente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mensajes_enviados')
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.remitente}: {self.contenido}'