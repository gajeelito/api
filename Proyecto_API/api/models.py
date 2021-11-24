from django.db import models

# Create your models here.

class Login(models.Model):
    correo=models.CharField(max_length=50)
    nombre=models.CharField(max_length=50)
    contrasenia=models.CharField(max_length=50)
