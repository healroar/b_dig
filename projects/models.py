from django.db import models

# Create your models here.

class Facultad(models.Model):
    cod_facultad = models.CharField(max_length=12, primary_key=True)
    nom_facultad = models.CharField(max_length=255, null=True, blank=True)
    icono = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.nom_facultad

class Carrera(models.Model):
    cod_carrera = models.CharField(max_length=30, primary_key=True)
    nom_carrera = models.CharField(max_length=255, null=False, blank=True)
    grado = models.CharField(max_length=100, null=True, blank=True)
    cod_facultad = models.ForeignKey(Facultad, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom_carrera

class Asignatura(models.Model):
    cod_asig = models.CharField(max_length=12, default='SIN_CODIGO')
    nom_asig = models.CharField(max_length=255)
    cod_carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    semestre = models.IntegerField(default=0)

    def __str__(self):
        return self.nom_asig

class Libro(models.Model):
    libro = models.CharField(max_length=255, null=True, blank=True)
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255, null=True, blank=True)
    control = models.CharField(max_length=20, null=True, blank=True)
    editorial = models.CharField(max_length=255, null=True, blank=True)
    edicion = models.CharField(max_length=30, null=True, blank=True)
    publicacion = models.CharField(max_length=100, null=True, blank=True)
    anio = models.IntegerField(null=True, blank=True)
    tipo = models.CharField(max_length=20, null=True, blank=True)
    catalogo = models.CharField(max_length=500, null=True, blank=True)
    ebook = models.CharField(max_length=500, null=True, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['libro'], name='indice_libro')
        ]

    def __str__(self):
        return self.titulo

class LibroAsignatura(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.libro.titulo} - {self.asignatura.nombre}"
