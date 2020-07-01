from django.contrib import admin
from .models import *

@admin.register(Cliente)
class ClienteAdmin (admin.ModelAdmin):
    list_display = ['rut' , 'nombre', 'telefono']
    list_filter = ['nombre' , 'telefono']

@admin.register(Producto)
class ProductoAdmin (admin.ModelAdmin):
    fieldsets = (('Descripcion', {'fields': ('idd', 'nombre',)}) , ('Variable', {'fields': ('precio', 'stock' )}), )


class ProductoInLine(admin.TabularInline):
    model = Producto

@admin.register(Proveedore)
class ProveedoreFilt(admin.ModelAdmin):
    list_display = ['rut', 'nombre' , 'direccion', 'telefono']
    list_display_links = ['rut' , 'nombre'] 
    list_filter = ['nombre',]
    inlines = [ProductoInLine, ]

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin): 
    list_display = ['fecha', 'cliente', 'isDescuento']
    list_display_links = ['fecha' , 'cliente', ]
    actions = ['desconta']

    def desconta (self,request,queryset):
        return queryset.update(descuento = True)


# Register your models here.
admin.site.register(Categoria)
admin.site.register(Direccion)
