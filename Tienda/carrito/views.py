from django.shortcuts import render, redirect


from .carrito import carrito
from tiendaDeportes.models import Producto,Pedido

def agregar_producto(request, producto_id):
    Carrito=carrito(request)
    producto=Producto.objects.get(id=producto_id)
    Carrito.agregar(producto)
    return redirect("Index")

def restar_producto(request, producto_id):
     Carrito=carrito(request)
     producto=Producto.objects.get(id=producto_id)
     Carrito.restar(producto)
     return redirect("Index")

def limpiar_carrito(request):
     Carrito=carrito(request)
     Carrito.limpiarCarrito()
     return redirect("Index")

def carrini(request):
    return render(request,"carrito.html")

def pedidolisto(request):
     if request.user.is_authenticated:
          for key, value in request.session["carrito"].items():
               usuario=request.user
               nombreProducto=value["nombre"]
               precio=value["precio"]
               cantidad=value["cantidad"]
               pedido=Pedido.objects.create(Usuario=usuario,NombreProducto=nombreProducto,Precio=precio,Cantidad=cantidad)
          limpiar_carrito(request)
          return render(request,"pedido.html")
     else:
          return render(request,"autenticar.html")