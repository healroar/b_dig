from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Libro, Asignatura, LibroAsignatura, Facultad, Carrera
from .serializers import LibroSerializer, AsignaturaSerializer, LibroAsignaturaSerializer, FacultadSerializer, CarreraSerializer

class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

class AsignaturaViewSet(viewsets.ModelViewSet):
    queryset = Asignatura.objects.all()
    serializer_class = AsignaturaSerializer

class LibroAsignaturaViewSet(viewsets.ModelViewSet):
    queryset = LibroAsignatura.objects.all()
    serializer_class = LibroAsignaturaSerializer

class FacultadViewSet(viewsets.ModelViewSet):
    queryset = Facultad.objects.all()
    serializer_class = FacultadSerializer

class CarreraViewSet(viewsets.ModelViewSet):
    queryset = Carrera.objects.all()
    serializer_class = CarreraSerializer