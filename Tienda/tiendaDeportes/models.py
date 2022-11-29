from django.db import models

# Create your models here.
class Producto(models.Model):
    Nombre= models.CharField(max_length=50)
    imagen=models.ImageField(upload_to="tiendaDeportes",null=True,blank=True)
    precio=models.FloatField()
    stock=models.IntegerField()
    TIPO_PRODUCTO_CHOICES=[
        (1,'Normal'),
        (2,'Popular'),
        (3,'Promo'),
 ]
    tipo=models.IntegerField(choices=TIPO_PRODUCTO_CHOICES,default=1)
    created=models.DateTimeField(auto_now_add=True, auto_now=False)
    updated=models.DateTimeField(auto_now_add=True, auto_now=False)

class Meta:
    verbose_name='Producto'
    verbose_name_plural='Productos'

def __str__(self):
    return self.Nombre

class Pedido(models.Model):
    Usuario=models.CharField(max_length=50)
    NombreProducto=models.CharField(max_length=50)
    Precio=models.FloatField()
    Cantidad=models.IntegerField()
    created=models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name='Pedido'
        verbose_name_plural='Pedidos'

    def __str__(self):
        return self.Usuario+""+self.NombreProducto