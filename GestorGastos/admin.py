from django.contrib import admin

from .models import Usuario, Gasto, Ingreso, CategoriaGasto

admin.site.register(Usuario)
admin.site.register(Gasto)
admin.site.register(Ingreso)
admin.site.register(CategoriaGasto)
