from rest_framework import status, views
from rest_framework.response import Response
from authApp.serializers.acudienteSerializer import acudienteSerializer
from authApp.models.acudiente import acudiente

class acudienteDetail (views.APIView):
    def get(self,request,pk,format= None):
        model=acudiente.objects.get(pk=pk)
        serializer=acudienteSerializer(model)
        return Response(serializer.data)
