from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import UsuarioSerializer, CategoriaGastoSerializer, GastoSerializer, IngresoSerializer
from .models import Usuario, CategoriaGasto, Gasto, Ingreso

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all().order_by('nombre')
    serializer_class = UsuarioSerializer

class CategoriaGastoViewSet(viewsets.ModelViewSet):
    queryset = CategoriaGasto.objects.all().order_by('nombre')
    serializer_class = CategoriaGastoSerializer


class GastoViewSet(viewsets.ModelViewSet):
    queryset = Gasto.objects.all().order_by('fecha')
    serializer_class = GastoSerializer

class IngresoViewSet(viewsets.ModelViewSet):
    queryset = Ingreso.objects.all().order_by('fecha')
    serializer_class = IngresoSerializer