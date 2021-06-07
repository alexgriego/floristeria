from django.contrib import admin

from .models import Oferta, Compra, Cliente, Inventario_de_flores

class OfertaAdmin(admin.ModelAdmin):
    list_display = ('flores_en_descuento', 'valor_de_descuento', 'usuario_con_descuento')

class CompraAdmin(admin.ModelAdmin):
    list_display = ('valor_de_compra', 'fecha', 'numero_de_factura')

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'documento', 'direccion')

class Inventario_de_floresAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo', 'nit', 'temporada', 'ocasion')

# Register your models here.
admin.site.register(Oferta, OfertaAdmin)
admin.site.register(Compra, CompraAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Inventario_de_flores, Inventario_de_floresAdmin)