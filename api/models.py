from django.db import models
import datetime

class Producto(models.Model):
    productoNombre = models.CharField(max_length=200)
    productoDescripcion = models.CharField(blank=True , max_length=200)
    productoPrecio = models.DecimalField(max_digits=10,decimal_places=2)
    productoImagen = models.ImageField(null=True, blank=True , upload_to='images/')
    
    def __str__(self):
        return self.productoNombre

class Persona(models.Model):
    nombre = models.CharField('Nombre',max_length=100)
    apellido = models.CharField('Apellido',max_length=200)
    foto = models.ImageField(null=True,blank=True,upload_to='fotos/')
    class Meta:
        abstract = True

class Cliente(Persona):
    email = models.EmailField(blank=True)

    def __str__(self):
        return '{0},{1}'.format(self.apeliido , self.nombre)
    
class Venta(models.Model):
    cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE, verbose_name='Cliente ok ' , null=False)
    fecha = models.DateTimeField(default=datetime.datetime.now)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return '{0}'.format(self.id)

class VentaProducto(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE,verbose_name='Nro Venta',null=False)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE,verbose_name='Producto',null=False)
    cantidad = models.PositiveBigIntegerField(default=0)
    precio_unidad = models.FloatField()
    modificacion = models.DateTimeField(auto_now_add=True)
    estado = models.BooleanField(default=True)
    def __str__(self):
        return f'{self.venta} to {self.producto}'
    
class Meta:
    indexes =[
        models.Index(fields=['venta','producto']),
    ]