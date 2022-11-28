from django.shortcuts import render, redirect
from .carrito import carrito
from tiendaDeportes.models import Producto

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

def carrito(request):
    return render (request, "carrito.html")