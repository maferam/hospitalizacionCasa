from django.db import models
from .user import User

class paciente(models.Model):
    id_paciente = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='paciente', on_delete=models.CASCADE)
    nombre = models.CharField('nombre', max_length=45)
    fecha_nacimiento= models.DateField('fecha de nacimiento')
    direccion= models.CharField('dirección',max_length=45)