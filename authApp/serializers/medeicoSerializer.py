from authApp.models.medico import medico
from rest_framework import serializers

class medicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = medico
        fields = ['nombre', 'correo', 'rol']