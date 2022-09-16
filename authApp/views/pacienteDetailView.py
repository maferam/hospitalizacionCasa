from rest_framework import status, views
from rest_framework.response import Response
from authApp.serializers.pacienteSerializer import pacienteSerializer
from authApp.models.paciente import paciente

class pacienteDetail (views.APIView):
    def get(self,request,pk,format= None):
        model=paciente.objects.get(pk=pk)
        serializer=pacienteSerializer(model)
        return Response(serializer.data)

        

