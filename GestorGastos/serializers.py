from rest_framework import serializers

from .models import Usuario, CategoriaGasto, Gasto, Ingreso


class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Usuario
        fields=('nombre','correo','contrasenia','saldo')


class CategoriaGastoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=CategoriaGasto
        fields=('nombre','descripcion')


class GastoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Gasto
        fields=('fecha','monto','descripcion','categoria','usuario')

class IngresoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Ingreso
        fields=('fecha','monto','fuente','descripcion','usuario')