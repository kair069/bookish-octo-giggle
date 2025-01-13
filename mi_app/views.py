from django.shortcuts import render

from django.shortcuts import render

def home(request):
    # if not request.user.is_authenticated:  # Verifica si el usuario está autenticado
    #     return redirect('login_usuario')  # Redirige al login si no está autenticado
    return render(request, 'mi_app/home.html')

def about(request):
    return render(request, 'mi_app/about.html')

def contact(request):
    return render(request, 'mi_app/contact.html')


  
#3♣3♣35#3♣3♣35353535#                                      MARCAS

from django.shortcuts import render, redirect, get_object_or_404
from .models import Marca
from .forms import MarcaForm

# Vista para crear una nueva marca
def crear_marca(request):
    if request.method == 'POST':
        form = MarcaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_marcas')  # Redirigir a la lista de marcas
    else:
        form = MarcaForm()
    return render(request, 'mi_app/marcas/crear_marca.html', {'form': form})

# Vista para listar todas las marcas
def listar_marcas(request):
    marcas = Marca.objects.all()
    return render(request, 'mi_app/marcas/listar_marcas.html', {'marcas': marcas})

# Vista para actualizar una marca existente
def actualizar_marca(request, pk):
    marca = get_object_or_404(Marca, pk=pk)
    if request.method == 'POST':
        form = MarcaForm(request.POST, instance=marca)
        if form.is_valid():
            form.save()
            return redirect('listar_marcas')  # Redirigir a la lista de marcas
    else:
        form = MarcaForm(instance=marca)
    return render(request, 'mi_app/marcas/actualizar_marca.html', {'form': form, 'marca': marca})

# Vista para eliminar una marca
def eliminar_marca(request, pk):
    marca = get_object_or_404(Marca, pk=pk)
    if request.method == 'POST':
        marca.delete()
        return redirect('listar_marcas')  # Redirigir a la lista de marcas
    return render(request, 'mi_app/marcas/eliminar_marca.html', {'marca': marca})



#3♣3♣35#3♣3♣35353535#                                      CATEGORIAS

from django.shortcuts import render, get_object_or_404, redirect
from .models import Categoria
from .forms import CategoriaForm


def listar_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'mi_app/categorias/listar_categorias.html', {'categorias': categorias})


def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_categorias')  # Asegúrate de tener una URL configurada
    else:
        form = CategoriaForm()
    
    return render(request, 'mi_app/categorias/crear_categoria.html', {'form': form})



def actualizar_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('listar_categorias')
    else:
        form = CategoriaForm(instance=categoria)
    
    return render(request, 'mi_app/categorias/actualizar_categoria.html', {'form': form})


def eliminar_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    
    if request.method == 'POST':
        categoria.delete()
        return redirect('listar_categorias')
    
    return render(request, 'mi_app/categorias/eliminar_categoria.html', {'categoria': categoria})


#3♣3♣35#3♣3♣35353535#                                      tipo moto
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages
from .models import TipoMotor
from .forms import TipoMotorForm

# Listar Tipos de Motor
def listar_tipos_motor(request):
    tipos_motor = TipoMotor.objects.all()
    return render(request, 'mi_app/tipomotor/listar.html', {'tipos_motor': tipos_motor})

# Crear Tipo de Motor
def crear_tipo_motor(request):
    if request.method == 'POST':
        form = TipoMotorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tipo de motor creado exitosamente.')
            return redirect('listar_tipos_motor')
        else:
            messages.error(request, 'Hubo un error al crear el tipo de motor.')
    else:
        form = TipoMotorForm()
    return render(request, 'mi_app/tipomotor/form.html', {'form': form})

# Editar Tipo de Motor
def editar_tipo_motor(request, pk):
    tipo_motor = get_object_or_404(TipoMotor, pk=pk)
    if request.method == 'POST':
        form = TipoMotorForm(request.POST, instance=tipo_motor)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tipo de motor actualizado correctamente.')
            return redirect('listar_tipos_motor')
        else:
            messages.error(request, 'Hubo un error al actualizar el tipo de motor.')
    else:
        form = TipoMotorForm(instance=tipo_motor)
    return render(request, 'mi_app/tipomotor/form.html', {'form': form})

# Eliminar Tipo de Motor
def eliminar_tipo_motor(request, pk):
    tipo_motor = get_object_or_404(TipoMotor, pk=pk)
    if request.method == 'POST':
        tipo_motor.delete()
        messages.success(request, 'Tipo de motor eliminado exitosamente.')
        return redirect('listar_tipos_motor')
    return render(request, 'mi_app/tipomotor/confirmar_eliminar.html', {'tipo_motor': tipo_motor})


#3♣3♣35#3♣3♣35353535#                                      producto

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Producto, Marca, Categoria, TipoMotor
from .forms import ProductoForm

# Listar Productos

# def listar_productos(request):
#     productos = Producto.objects.select_related('marca', 'categoria', 'tipo_motor').all()
#     return render(request, 'mi_app/producto/listar.html', {'productos': productos})

from django.db.models import Q
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Producto

def listar_productos(request):
    # Inicializar la consulta básica para seleccionar relaciones de los productos
    productos_list = Producto.objects.select_related('marca', 'categoria', 'tipo_motor')

     # Obtener los parámetros de búsqueda desde la solicitud GET
    nombre = request.GET.get('nombre', '')
    marca = request.GET.get('marca', '')
    qr_code = request.GET.get('qr_code', '')
    categoria = request.GET.get('categoria', '')

     # Crear un filtro dinámico usando Q para poder combinar condiciones
    filtros = Q()
    # Aplicar filtros solo si tienen valor
    if nombre:
        filtros &= Q(nombre_producto__icontains=nombre)  # Filtrar por nombre del producto
    if marca:
        filtros &= Q(marca__nombre_marca__icontains=marca)  # Filtrar por nombre de la marca
    if qr_code:
        filtros &= Q(qr_code__icontains=qr_code)  # Filtrar por código QR
    if categoria:
        filtros &= Q(categoria__nombre_categoria__icontains=categoria)  # Filtrar por nombre de categoría


    # Aplicar los filtros solo si se han añadido
    if filtros != Q():
        productos_list = productos_list.filter(filtros)

    # Paginación: 4 productos por página
    paginator = Paginator(productos_list, 4)
    page = request.GET.get('page')

    try:
        productos = paginator.get_page(page)
    except:
        productos = paginator.get_page(1)  # Si la página no es válida, cargar la primera página

    # Mantener los filtros en la URL para la paginación
    base_url = '?'
    if nombre:
        base_url += f'nombre={nombre}&'
    if marca:
        base_url += f'marca={marca}&'
    if qr_code:
        base_url += f'qr_code={qr_code}&'

    # Eliminar el último '&' si existe
    if base_url.endswith('&'):
        base_url = base_url[:-1]

    marcas = Marca.objects.all()
    categorias = Categoria.objects.all()
    return render(request, 'mi_app/producto/listar.html', {
        'productos': productos,
        'nombre': nombre,
        'marca': marca,
        'qr_code': qr_code,
        'categoria': categoria,
        'marcas': marcas,
        'categorias': categorias,
    })





# Crear Producto
def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto creado exitosamente.')
            return redirect('listar_productos')
        else:
            messages.error(request, 'Hubo un error al crear el producto.')
    else:
        form = ProductoForm()
    return render(request, 'mi_app/producto/form.html', {'form': form})

# Editar Producto
def editar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto actualizado correctamente.')
            return redirect('listar_productos')
        else:
            messages.error(request, 'Hubo un error al actualizar el producto.')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'mi_app/producto/form.html', {'form': form})

# Eliminar Producto
def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        messages.success(request, 'Producto eliminado exitosamente.')
        return redirect('listar_productos')
    return render(request, 'mi_app/producto/confirmar_eliminar.html', {'producto': producto})

## mas funcionalidaddes producto
from decimal import Decimal

def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)

    # Realizamos el cálculo del precio sin IVA
    precio_sin_iva = producto.precio / Decimal('1.18')  # Convertir el 1.18 a Decimal

    # Consultamos el tipo de motor
    tipo_motor = producto.tipo_motor

    # Contexto a pasar a la plantilla
    context = {
        'producto': producto,
        'precio_sin_iva': precio_sin_iva,
        'tipo_motor': tipo_motor,
    }

    return render(request, 'mi_app/producto/detalle.html', context)





#3♣3♣35#3♣3♣35353535#                                      tipo producto

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import TipoProducto
from .forms import TipoProductoForm

# Vista para listar todos los tipos de productos
def tipo_producto_list(request):
    tipo_productos = TipoProducto.objects.all()
    return render(request, 'mi_app/tipo_producto/tipo_producto_list.html', {'tipo_productos': tipo_productos})

# Vista para crear un nuevo tipo de producto
def tipo_producto_create(request):
    if request.method == 'POST':
        form = TipoProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tipo_productos_listar')  # Redirección a la vista de listar productos
    else:
        form = TipoProductoForm()
    return render(request, 'mi_app/tipo_producto/tipo_producto_form.html', {'form': form})

# Vista para editar un tipo de producto existente
def tipo_producto_edit(request, pk):
    tipo_producto = get_object_or_404(TipoProducto, pk=pk)
    if request.method == 'POST':
        form = TipoProductoForm(request.POST, instance=tipo_producto)
        if form.is_valid():
            form.save()
            return redirect('tipo_productos_listar')  # Redirección a la vista de listar productos
    else:
        form = TipoProductoForm(instance=tipo_producto)
    return render(request, 'mi_app/tipo_producto/tipo_producto_form.html', {'form': form})

# Vista para eliminar un tipo de producto
def tipo_producto_delete(request, pk):
    tipo_producto = get_object_or_404(TipoProducto, pk=pk)
    if request.method == 'POST':
        tipo_producto.delete()
        return redirect('tipo_productos_listar')  # Redirección a la vista de listar productos
    return render(request, 'mi_app/tipo_producto/tipo_producto_confirm_delete.html', {'tipo_producto': tipo_producto})


#3♣3♣35#3♣3♣35353535#                                      producto tipo


from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import ProductoTipo, Producto, TipoProducto
from .forms import ProductoTipoForm

# Vista para listar todas las relaciones Producto-TipoProducto
def producto_tipo_list(request):
    producto_tipos = ProductoTipo.objects.all()
    return render(request, 'mi_app/producto_tipo/tipo_producto_list.html', {'producto_tipos': producto_tipos})

# Vista para crear una nueva relación entre Producto y TipoProducto
def producto_tipo_create(request):
    if request.method == 'POST':
        form = ProductoTipoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'La relación Producto-TipoProducto se ha creado correctamente.')
            return redirect('producto_tipo_list')
        else:
            messages.error(request, 'Por favor, corrige los errores en el formulario.')
    else:
        form = ProductoTipoForm()

    return render(request, 'mi_app/producto_tipo/tipo_producto_form.html', {'form': form})

# Vista para editar una relación Producto-TipoProducto existente
def producto_tipo_edit(request, pk):
    producto_tipo = get_object_or_404(ProductoTipo, pk=pk)
    if request.method == 'POST':
        form = ProductoTipoForm(request.POST, instance=producto_tipo)
        if form.is_valid():
            form.save()
            messages.success(request, 'La relación Producto-TipoProducto se ha actualizado correctamente.')
            return redirect('producto_tipo_list')
        else:
            messages.error(request, 'Por favor, corrige los errores en el formulario.')
    else:
        form = ProductoTipoForm(instance=producto_tipo)
    
    return render(request, 'mi_app/producto_tipo/tipo_producto_form.html', {'form': form})

# Vista para eliminar una relación Producto-TipoProducto
def producto_tipo_delete(request, pk):
    producto_tipo = get_object_or_404(ProductoTipo, pk=pk)
    if request.method == 'POST':
        producto_tipo.delete()
        messages.success(request, 'La relación Producto-TipoProducto ha sido eliminada correctamente.')
        return redirect('producto_tipo_list')
    return render(request, 'mi_app/producto_tipo/tipo_producto_confirm_delete.html', {'producto_tipo': producto_tipo})


#3♣3♣35#3♣3♣35353535#                                      clientes
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Cliente
from .forms import ClienteForm

# Vista para listar clientes
def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'mi_app/clientes/listar_clientes.html', {'clientes': clientes})

# Vista para crear un nuevo cliente
def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente creado con éxito')
            return redirect('listar_clientes')
        else:
            messages.error(request, 'Hubo un error al crear el cliente')
    else:
        form = ClienteForm()
    
    return render(request, 'mi_app/clientes/crear_cliente.html', {'form': form})

# Vista para editar un cliente existente
def editar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente actualizado con éxito')
            return redirect('listar_clientes')
        else:
            messages.error(request, 'Hubo un error al actualizar el cliente')
    else:
        form = ClienteForm(instance=cliente)
    
    return render(request, 'mi_app/clientes/editar_cliente.html', {'form': form, 'cliente': cliente})

# Vista para eliminar un cliente
def eliminar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    if request.method == 'POST':
        cliente.delete()
        messages.success(request, 'Cliente eliminado con éxito')
        return redirect('listar_clientes')
    
    return render(request, 'mi_app/clientes/eliminar_cliente.html', {'cliente': cliente})



#3♣3♣35#3♣3♣35353535#                                      proveedores

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Proveedor
from .forms import ProveedorForm

# Vista para listar los proveedores
def listar_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'mi_app/proveedores/listar_proveedores.html', {'proveedores': proveedores})

# Vista para crear un nuevo proveedor
def crear_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Proveedor creado con éxito')
            return redirect('listar_proveedores')
        else:
            messages.error(request, 'Hubo un error al crear el proveedor')
    else:
        form = ProveedorForm()
    
    return render(request, 'mi_app/proveedores/crear_proveedor.html', {'form': form})

# Vista para editar un proveedor existente
def editar_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, pk=proveedor_id)
    if request.method == 'POST':
        form = ProveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            messages.success(request, 'Proveedor actualizado con éxito')
            return redirect('listar_proveedores')
        else:
            messages.error(request, 'Hubo un error al actualizar el proveedor')
    else:
        form = ProveedorForm(instance=proveedor)
    
    return render(request, 'mi_app/proveedores/editar_proveedor.html', {'form': form, 'proveedor': proveedor})

# Vista para eliminar un proveedor
def eliminar_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, pk=proveedor_id)
    if request.method == 'POST':
        proveedor.delete()
        messages.success(request, 'Proveedor eliminado con éxito')
        return redirect('listar_proveedores')
    
    return render(request, 'mi_app/proveedores/eliminar_proveedor.html', {'proveedor': proveedor})


#3♣3♣35#3♣3♣35353535#                                      Compra
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Compra
from .forms import CompraForm

# Vista para listar las compras
def listar_compras(request):
    compras = Compra.objects.all()  # Obtener todas las compras
    return render(request, 'mi_app/compras/listar_compras.html', {'compras': compras})

# Vista para crear una nueva compra
def crear_compra(request):
    if request.method == 'POST':
        form = CompraForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Compra creada con éxito')
            return redirect('listar_compras')
        else:
            messages.error(request, 'Hubo un error al crear la compra')
    else:
        form = CompraForm()  # Crear el formulario vacío
    
    return render(request, 'mi_app/compras/crear_compra.html', {'form': form})

# Vista para editar una compra existente
def editar_compra(request, compra_id):
    compra = get_object_or_404(Compra, pk=compra_id)
    
    if request.method == 'POST':
        form = CompraForm(request.POST, instance=compra)
        if form.is_valid():
            form.save()
            messages.success(request, 'Compra actualizada con éxito')
            return redirect('listar_compras')
        else:
            messages.error(request, 'Hubo un error al actualizar la compra')
    else:
        form = CompraForm(instance=compra)  # Crear el formulario con los datos de la compra
    
    return render(request, 'mi_app/compras/editar_compra.html', {'form': form, 'compra': compra})

# Vista para eliminar una compra
def eliminar_compra(request, compra_id):
    compra = get_object_or_404(Compra, pk=compra_id)
    
    if request.method == 'POST':
        compra.delete()
        messages.success(request, 'Compra eliminada con éxito')
        return redirect('listar_compras')
    
    return render(request, 'mi_app/compras/eliminar_compra.html', {'compra': compra})



#3♣3♣35#3♣3♣35353535#                                      Detalle de comprea


from django.shortcuts import render, get_object_or_404
from .models import Compra, DetalleCompra
from .forms import DetalleCompraForm
from django.contrib import messages
from django.shortcuts import redirect

# Vista para listar los detalles de la compra
def listar_detalles(request, compra_id):
    compra = get_object_or_404(Compra, pk=compra_id)
    detalles = DetalleCompra.objects.filter(compra=compra)
    return render(request, 'mi_app/decompras/listar_detalles.html', {'compra': compra, 'detalles': detalles})


def agregar_detalle(request, compra_id):
    compra = get_object_or_404(Compra, pk=compra_id)
    
    if request.method == 'POST':
        form = DetalleCompraForm(request.POST)
        if form.is_valid():
            detalle = form.save(commit=False)
            detalle.compra = compra  # Asociamos el detalle con la compra
            detalle.save()
            messages.success(request, 'Detalle de compra agregado con éxito')
            return redirect('listar_detalles', compra_id=compra.id)
        else:
            messages.error(request, 'Hubo un error al agregar el detalle')
    else:
        form = DetalleCompraForm()

    return render(request, 'mi_app/decompras/agregar_detalle.html', {'form': form, 'compra': compra})


def editar_detalle(request, compra_id, detalle_id):
    detalle = get_object_or_404(DetalleCompra, pk=detalle_id, compra__id=compra_id)
    
    if request.method == 'POST':
        form = DetalleCompraForm(request.POST, instance=detalle)
        if form.is_valid():
            form.save()
            messages.success(request, 'Detalle de compra actualizado con éxito')
            return redirect('listar_detalles', compra_id=compra_id)
        else:
            messages.error(request, 'Hubo un error al actualizar el detalle')
    else:
        form = DetalleCompraForm(instance=detalle)

    return render(request, 'mi_app/decompras/editar_detalle.html', {'form': form, 'compra': detalle.compra, 'detalle': detalle})

def eliminar_detalle(request, compra_id, detalle_id):
    detalle = get_object_or_404(DetalleCompra, pk=detalle_id, compra__id=compra_id)
    
    if request.method == 'POST':
        detalle.delete()
        messages.success(request, 'Detalle de compra eliminado con éxito')
        return redirect('listar_detalles', compra_id=compra_id)
    
    return render(request, 'mi_app/decompras/eliminar_detalle.html', {'detalle': detalle})



#                                                      ventas
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Venta, DetalleVenta
from .forms import VentaForm, DetalleVentaForm

# Vista para listar ventas
def listar_ventas(request):
    ventas = Venta.objects.all()
    return render(request, 'mi_app/ventas/listar_ventas.html', {'ventas': ventas})

# Crear nueva venta
def crear_venta(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Venta registrada con éxito')
            return redirect('listar_ventas')
    else:
        form = VentaForm()
    return render(request, 'mi_app/ventas/crear_venta.html', {'form': form})

# Editar venta
def editar_venta(request, venta_id):
    venta = get_object_or_404(Venta, pk=venta_id)
    if request.method == 'POST':
        form = VentaForm(request.POST, instance=venta)
        if form.is_valid():
            form.save()
            messages.success(request, 'Venta actualizada correctamente')
            return redirect('listar_ventas')
    else:
        form = VentaForm(instance=venta)
    return render(request, 'mi_app/ventas/editar_venta.html', {'form': form, 'venta': venta})

# Eliminar venta
def eliminar_venta(request, venta_id):
    venta = get_object_or_404(Venta, pk=venta_id)
    if request.method == 'POST':
        venta.delete()
        messages.success(request, 'Venta eliminada correctamente')
        return redirect('listar_ventas')
    return render(request, 'mi_app/ventas/eliminar_venta.html', {'venta': venta})


#                                                    Detalles Ventas

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import DetalleVenta, Venta, Producto
from .forms import DetalleVentaForm

# Listar detalles de una venta específica
def listar_detalles_venta(request, venta_id):
    venta = get_object_or_404(Venta, pk=venta_id)
    detalles = DetalleVenta.objects.filter(venta=venta)
    return render(request, 'mi_app/deventas/listar_detalles_venta.html', {'venta': venta, 'detalles': detalles})

# Agregar nuevo detalle a una venta
def agregar_detalle_venta(request, venta_id):
    venta = get_object_or_404(Venta, pk=venta_id)

    if request.method == 'POST':
        form = DetalleVentaForm(request.POST)
        if form.is_valid():
            detalle = form.save(commit=False)
            detalle.venta = venta
            detalle.save()
            messages.success(request, 'Detalle agregado con éxito.')
            return redirect('listar_detalles_venta', venta_id=venta.id)
        else:
            messages.error(request, 'Hubo un error al agregar el detalle.')
    else:
        form = DetalleVentaForm()

    return render(request, 'mi_app/deventas/agregar_detalle_venta.html', {'form': form, 'venta': venta})

# Editar detalle de una venta
def editar_detalle_venta(request, detalle_id):
    detalle = get_object_or_404(DetalleVenta, pk=detalle_id)
    venta = detalle.venta

    if request.method == 'POST':
        form = DetalleVentaForm(request.POST, instance=detalle)
        if form.is_valid():
            form.save()
            messages.success(request, 'Detalle actualizado con éxito.')
            return redirect('listar_detalles_venta', venta_id=venta.id)
        else:
            messages.error(request, 'Hubo un error al actualizar el detalle.')
    else:
        form = DetalleVentaForm(instance=detalle)

    return render(request, 'mi_app/deventas/editar_detalle_venta.html', {'form': form, 'venta': venta, 'detalle': detalle})

# Eliminar detalle de una venta
def eliminar_detalle_venta(request, detalle_id):
    detalle = get_object_or_404(DetalleVenta, pk=detalle_id)
    venta = detalle.venta

    if request.method == 'POST':
        detalle.delete()
        messages.success(request, 'Detalle eliminado con éxito.')
        return redirect('listar_detalles_venta', venta_id=venta.id)

    return render(request, 'mi_app/deventas/eliminar_detalle_venta.html', {'detalle': detalle, 'venta': venta})


##3♣                                               Tipo de  documento

from django.shortcuts import render, get_object_or_404, redirect
from .models import TipoDocumento
from .forms import TipoDocumentoForm

# Listar Tipos de Documento
def listar_tipos_documento(request):
    tipos_documento = TipoDocumento.objects.all()
    return render(request, 'mi_app/tipodocumento/listar_tipos_documento.html', {'tipos_documento': tipos_documento})

# Crear Nuevo Tipo de Documento
def crear_tipo_documento(request):
    if request.method == 'POST':
        form = TipoDocumentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_tipos_documento')
    else:
        form = TipoDocumentoForm()
    return render(request, 'mi_app/tipodocumento/form_tipo_documento.html', {'form': form})

# Editar Tipo de Documento
def editar_tipo_documento(request, pk):
    tipo_documento = get_object_or_404(TipoDocumento, pk=pk)
    if request.method == 'POST':
        form = TipoDocumentoForm(request.POST, instance=tipo_documento)
        if form.is_valid():
            form.save()
            return redirect('listar_tipos_documento')
    else:
        form = TipoDocumentoForm(instance=tipo_documento)
    return render(request, 'mi_app/tipodocumento/form_tipo_documento.html', {'form': form})

# Eliminar Tipo de Documento
def eliminar_tipo_documento(request, pk):
    tipo_documento = get_object_or_404(TipoDocumento, pk=pk)
    if request.method == 'POST':
        tipo_documento.delete()
        return redirect('listar_tipos_documento')
    return render(request, 'mi_app/tipodocumento/eliminar_tipo_documento.html', {'tipo_documento': tipo_documento})

from .calculadora_views import calculadora  # Importamos la vista

from .dashboards import dashboard_view # Importamos la vista
