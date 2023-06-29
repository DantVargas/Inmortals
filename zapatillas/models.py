from django.db import models

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
    marca =models.ForeignKey(Marca, on_delete=models.PROTECT)
    
    def __str__(self) :
        return self.nombre