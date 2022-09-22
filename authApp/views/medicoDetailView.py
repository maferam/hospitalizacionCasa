from rest_framework import status, views
from rest_framework.response import Response
from authApp.serializers.medicoSerializer import medicoSerializer
from authApp.models.medico import medico

class medicoDetail(views.APIView):
    def get(self,request,pk,format= None):
        model=medico.objects.get(pk=pk)
        serializer=medicoSerializer(model)
        return Response(serializer.data)
