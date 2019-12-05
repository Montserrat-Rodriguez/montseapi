from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework import routers, serializers, viewsets
from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework import status


from django.shortcuts import get_object_or_404
from django.http import Http404

import time

#IsAuthenticated


from example.models import Alumnos

from example.models import Carrera

from example.serializer import AlumnosSerializer
from example.serializer import CarreraSerializer

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class CarreraList(APIView):
    
    def get(self, request, format=None):
        queryset = Carrera.objects.all()
        serializer = CarreraSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = CarreraSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class CarreraDetail(APIView):
    def get_object(self, id):
        try:
            return Carrera.objects.get(pk=id)
        except Carrera.DoesNotExist:
            return False
    
    def get(self, request, id, format=None):
        example = self.get_object(id)
        if example != False:
            serializer = CarreraSerializer(example)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        Carrera.objects.get(pk=id).delete()
        return Response("ok")
    
    def put(self, request, id, format=None):
        example = self.get_object(id)
        if example != False:
            serializer = CarreraSerializer(example, data=request.data)
            if serializer.is_valid():
                serializer.save()
                datas = serializer.data
                return Response(datas)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class CarreraListAll(APIView):
    def get(self, request, format=None):
        queryset = Carrera.objects.all()
        serializer = CarreraviewSerializer(queryset, many=True)
        return Response(serializer.data)
         

#//////////////////////////////////////////////////////////////////////////////////////////////

class AlumnosList(APIView):    
    def get(self, request, format=None):
        queryset = Alumnos.objects.all()
        serializer = AlumnosSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = AlumnosSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class AlumnostListNombre(APIView):
    def get(self, request, nombre1, format=None):
        queryset = Alumnos.objects.filter(nombre=nombre1)
        serializer = AlumnosSerializer(queryset, many=True)
        return Response(serializer.data)

class AlumnostListEdad(APIView):
    def get(self, request, edad1, format=None):
        queryset = Alumnos.objects.filter(edad=edad1)
        serializer = AlumnosSerializer(queryset, many=True)
        return Response(serializer.data)

class AlumnostListCarrera(APIView):
    def get(self, request, carrera1, format=None):
        queryset = Alumnos.objects.filter(carrera_id=carrera1)
        serializer = AlumnosSerializer(queryset, many=True)
        return Response(serializer.data)

class AlumnostListAll(APIView):
    def get(self, request, format=None):
        queryset = Alumnos.objects.filter()
        serializer = AlumnosSerializer(queryset, many=True)
        return Response(serializer.data)

class AlumnosDetail(APIView):
    def get_object(self, id):
        try:
            return Alumnos.objects.get(pk=id)
        except Alumnos.DoesNotExist:
            return False
    
    def get(self, request, id, format=None):
        example = self.get_object(id)
        if example != False:
            serializer = AlumnosSerializer(example)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        Alumnos.objects.get(pk=id).delete()
        return Response("ok") 
    
    def put(self, request, id, format=None):
        example = self.get_object(id)
        if example != False:
            serializer = AlumnosSerializer(example, data=request.data)
            if serializer.is_valid():
                serializer.save()
                datas = serializer.data
                return Response(datas)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)







