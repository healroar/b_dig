from rest_framework import routers
from django.urls import path, include
from .views import LibroViewSet, AsignaturaViewSet, LibroAsignaturaViewSet

router = routers.DefaultRouter()
router.register(r'libros', LibroViewSet)
router.register(r'asignaturas', AsignaturaViewSet)
router.register(r'libros-asignaturas', LibroAsignaturaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]