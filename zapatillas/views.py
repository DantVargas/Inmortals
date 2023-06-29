from django.shortcuts import render, redirect,get_object_or_404
from .models import Producto
from .forms import ProductoForm

#Create your views here.
def index(request):
   
    productos = Producto.objects.all()
    data = {"productos" : productos}
    return render(request,'zapatillas/index.html',data)

def zapatillas_basquetball(request):
   
    productos = Producto.objects.all()
    data = {"productos" : productos}
    return render(request,'zapatillas/zapatillas_basquetball.html',data)


def agregar_producto(request):
    data = {'form': ProductoForm()}

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Se guardo un producto nuevo"
        else:
            data["form"] = formulario


    return render(request, 'zapatillas/producto/agregarzapatillas.html', data)

def listar_producto(request):
    productos = Producto.objects.all()
    data = {'productos' : productos}
    return render(request,'zapatillas/producto/listarzapatillas.html',data)

def editar_producto(request,id):
    producto = get_object_or_404(Producto, id=id)
    data = {'form' : ProductoForm(instance=producto)}
    
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Se modifico el producto correctamente"
            return redirect(to="listar_zapatillas")

    return render(request,'zapatillas/producto/editarzapatillas.html',data)

def eliminar_producto(request,id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    return redirect(to="listar_zapatillas")



