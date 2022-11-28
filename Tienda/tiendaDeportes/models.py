from django.db import models

# Create your models here.
class Producto(models.Model):
    Nombre= models.CharField(max_length=50)
    imagen=models.ImageField(upload_to="tiendaDeportes",null=True,blank=True)
    precio=models.FloatField()
    stock=models.IntegerField()
    created=models.DateTimeField(auto_now_add=True, auto_now=False)
    updated=models.DateTimeField(auto_now_add=True, auto_now=False)

class Meta:
    verbose_name='Producto'
    verbose_name_plural='Productos'

def __str__(self):
    return self.Nombre