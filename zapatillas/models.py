from django.db import models

# Create your models here.
class Marca(models.Model):
    nombre= models.CharField(max_length=50)


class Producto(models.Model):
    id_zapatillas = models.CharField( primary_key=True, max_length=10),
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    color = models.CharField(max_length=50)
    marca =models.ForeignKey(Marca, on_delete=models.PROTECT)
    