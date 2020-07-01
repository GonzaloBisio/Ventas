from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Venta)
admin.site.register(Categoria)
admin.site.register(Direccion)

@admin.register(Cliente)
class ClienteAdmin (admin.ModelAdmin):
    list_display = ['rut' , 'nombre', 'telefono']

@admin.register(Producto)
class ProductoAdmin (admin.ModelAdmin):
     fieldset = (('Descripción',{'fields ' :('idd', 'nombre')}), ('Variables', {'fields': ('precio' , 'stock')}))

@admin.register(Proveedore)
class ProveedoreFilter(admin.ModelAdmin):
    class Meta:
        model = Proveedore
        fields = ['nombre', 'rut']  