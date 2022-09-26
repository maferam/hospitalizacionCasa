from django.db import models
from .user import User


class medico(models.Model):
    id_medico = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='acudiente', on_delete=models.CASCADE)
    nombre = models.CharField('nombre', max_length=45)
    correo= models.EmailField('Correo',max_length=45)
    rol= models.CharField('rol',max_length=45)