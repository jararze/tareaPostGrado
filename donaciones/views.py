from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Causa, Donacion, Usuario, Categoria, Comentario
from .serializers import CausaSerializer, DonacionSerializer, UsuarioSerializer, CategoriaSerializer, ComentarioSerializer
from django.db.models import Sum

class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ComentarioViewSet(ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

class CausaViewSet(ModelViewSet):
    queryset = Causa.objects.all()
    serializer_class = CausaSerializer

class DonacionViewSet(ModelViewSet):
    queryset = Donacion.objects.all()
    serializer_class = DonacionSerializer

def api_total_donaciones(request):
    total_donations = 1000
    return JsonResponse({"total_donaciones": total_donations})

def landing_page(request):
    return render(request, 'donaciones/index.html')

# @api_view(['GET'])
# def resumen_donaciones(request):
#     causas = Causa.objects.all()
#     resumen = {causa.titulo: sum(d.monto for d in causa.donaciones.all()) for causa in causas}
#     return Response(resumen)

@api_view(['GET'])
def api_resumen_donaciones(request):
    # Obtener todas las causas con el total de donaciones asociadas
    causas = Causa.objects.all()
    resumen = []

    for causa in causas:
        total_donaciones = Donacion.objects.filter(causa=causa).aggregate(Sum('monto'))['monto__sum'] or 0
        resumen.append({
            "causa": causa.titulo,
            "descripcion": causa.descripcion,
            "monto_objetivo": causa.monto_objetivo,
            "total_donaciones": total_donaciones,
            "estado": "Completada" if total_donaciones >= causa.monto_objetivo else "En progreso"
        })

    # Calcular el total general de todas las donaciones
    total_general = Donacion.objects.aggregate(Sum('monto'))['monto__sum'] or 0

    return Response({
        "resumen_causas": resumen,
        "total_general": total_general
    })