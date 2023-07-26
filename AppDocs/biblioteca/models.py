# models.py

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# class MiUsuarioManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError('El email debe ser proporcionado')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser debe tener is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser debe tener is_superuser=True.')

#         return self.create_user(email, password, **extra_fields)

# class MiUsuario(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(unique=True)
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)

#     objects = MiUsuarioManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['first_name', 'last_name']

#     def __str__(self):
#         return self.email


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
