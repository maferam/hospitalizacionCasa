from authApp.models.acudiente import acudiente
from rest_framework import serializers

class acudienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = acudiente
        fields = ['parentesco', 'correo', 'nombre']