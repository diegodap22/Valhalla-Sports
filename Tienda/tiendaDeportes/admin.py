from django.contrib import admin

from .models import Pedido, Producto

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    readonly_fields=("created","updated")
    
admin.site.register(Producto,ProductoAdmin)

class PedidoAdmin(admin.ModelAdmin):
    readonly_fields=("created",)
admin.site.register(Pedido,PedidoAdmin)
