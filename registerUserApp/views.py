from __future__ import print_function
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.http import JsonResponse
from .models import Usuario
from .serializers import UsuarioSerializer


def ping(request):
    data = {"ping": "pong!"}
    return JsonResponse(data)

class UsuariosList(APIView):

    def post(self, request):
        token = request.data.get('token', '')
        if(token != 'f82779ddfbf8ccd5f1d48cc4986fd2d9'):
            return Response(email, status=status.HTTP_401_NOT_FOUND)

        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        token = request.data.get('token', '')
        if(token != 'f82779ddfbf8ccd5f1d48cc4986fd2d9'):
            return Response(email, status=status.HTTP_401_NOT_FOUND)
        usuarios = Usuario.objects.all().order_by('created_at')
        serializer = UsuarioSerializer(usuarios, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)