from django.shortcuts import render
from tiendaDeportes.models import Producto

# Create your views here.
def index(request):
    productos = Producto.objects.all().order_by("Nombre")
    return render (request, "index.html", {"productos": productos})
