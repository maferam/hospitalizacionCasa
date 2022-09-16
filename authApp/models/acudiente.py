from django.db import models
from .user import User
from.paciente import paciente

class acudiente(models.Model):
    id_acudiente = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='acudiente', on_delete=models.CASCADE)
    id_paciente= models.ForeignKey(paciente, related_name='acudiente', on_delete=models.CASCADE)
    parentesco = models.CharField('parentesco', max_length=45)
    correo= models.EmailField('Correo',max_length=45)
    nombre= models.CharField('Nombre',max_length=45)