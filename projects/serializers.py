from rest_framework import serializers
from .models import Libro, Asignatura, LibroAsignatura, Facultad, Carrera

class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = '__all__'

class AsignaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asignatura
        fields = '__all__'

class LibroAsignaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibroAsignatura
        fields = '__all__'

class FacultadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facultad
        fields = '__all__'

class CarreraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrera
        fields = '__all__'