from authApp.models.paciente import paciente
from rest_framework import serializers
class pacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = paciente
        fields = ['nombre', 'fecha_nacimiento', 'direccion']