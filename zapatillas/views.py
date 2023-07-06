from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Item_carrito
from .forms import ProductoForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


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

   
def producto_zapatilla(request, id):
    producto = get_object_or_404(Producto, id=id)
    data = {"producto" : producto}
    
    return render(request, 'zapatillas/producto_zapatilla.html', data)



def vista_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('zapatillas/index.html')  # Redirige a la página principal después del inicio de sesión
        else:
            error_message = 'Usuario o contraseña incorrectos.'
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')

def vista_logout(request):
    logout(request)
    return redirect('login')  # Redirige al formulario de inicio de sesión después del cierre de sesión



def carrito(request):
    
    item_carrito = Item_carrito.objects.all()
    context = {
        'item_carrito': item_carrito
    }
    return render(request, 'zapatillas/carrito.html', context)


@login_required
def agregar_carrito(request, id):
    producto = get_object_or_404(Producto, id=id)

    # Verificar si el producto ya está en el carrito
    item_carrito = Item_carrito.objects.filter(producto=producto, user=request.user).first()
    if item_carrito:
        # Si el producto ya está en el carrito, aumentar la cantidad
        item_carrito.quantity += 1
        item_carrito.save()
    else:
        # Si el producto no está en el carrito, crear un nuevo elemento en el carrito
        item_carrito = Item_carrito.objects.create(user=request.user, producto=producto)

    return redirect(to='carrito') 

@login_required
def eliminar_carrito(request, id):
    item_carrito = get_object_or_404(Item_carrito, id=id, user=request.user)
    item_carrito.delete()
    return redirect('carrito') 



def sobre_nosotros(request):
   
    productos = Producto.objects.all()
    data = {"productos" : productos}
    return render(request,'zapatillas/sobre_nosotros.html',data)
