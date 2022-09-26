from rest_framework import status, views
from rest_framework.response import Response
from authApp.serializers.medicoSerializer import medicoSerializer
from authApp.models.medico import medico
from urllib import request

class medicoCreate(views.APIView):
    def post(self,request,format=None):
        serializer=medicoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)