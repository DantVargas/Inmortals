from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Marca(models.Model):
    nombre= models.CharField(max_length=50)

    def __str__(self) :
        return self.nombre

class Producto(models.Model):
    id_zapatillas = models.CharField( primary_key=True, max_length=10),
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    color = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to="productos", null=True)
    imagen2 = models.ImageField(upload_to="productos", null=True)
    imagen3 = models.ImageField(upload_to="productos", null=True)
    marca =models.ForeignKey(Marca, on_delete=models.PROTECT)
    
    def __str__(self) :
        return self.nombre
    

class Item_carrito(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    quantity  = models.PositiveIntegerField(default=1)
    def __str__(self):
        return f"{self.user.username}'s Cart: {self.producto.nombre} x {self.quantity }"     
    


    