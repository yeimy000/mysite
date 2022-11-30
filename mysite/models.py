
from django.db import models

class Usuario(models.Model):
    username = models.CharField(max_length= 25, primary_key=True)
    password  = models.CharField(null=False, max_length=40, unique= True)
    email = models.CharField(null=False, max_length=60)
    nombre = models.CharField(null=False, max_length= 60)
    perfil = models.IntegerField(null=False)