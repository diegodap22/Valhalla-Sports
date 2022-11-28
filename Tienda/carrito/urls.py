from django.urls import path
from . import views

app_name="carrito"

urlpatterns=[
    path('',views.carrito, name="carrito"),
    path('agregar/<int:producto_id>/',views.agregar_producto, name="agregar"),
    path('restar/<int:producto_id>/',views.restar_producto, name="restar"),
]