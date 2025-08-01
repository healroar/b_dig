from rest_framework import serializers
from .models import Libro, Asignatura, LibroAsignatura

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
