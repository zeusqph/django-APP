from django.contrib import admin

from api.models import Producto,Cliente,Venta,VentaProducto

admin.site.register(Producto)
admin.site.register(Cliente)
admin.site.register(Venta)
admin.site.register(VentaProducto)
