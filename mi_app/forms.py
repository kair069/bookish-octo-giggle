from .models import Marca
from django import forms


#### ---------------------------------------MARCAS--------------------------------------- ####

class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ['nombre_marca']
        widgets = {
            'nombre_marca': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre de la marca'}),
        }

    def clean_nombre_marca(self):
        nombre_marca = self.cleaned_data.get('nombre_marca')
        if not nombre_marca:
            raise forms.ValidationError('El nombre de la marca no puede estar vacío.')
        return nombre_marca

#### ---------------------------------------Categorias--------------------------------------- ####

from django import forms
from .models import Categoria

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre_categoria']
        labels = {
            'nombre_categoria': 'Nombre de la Categoría'
        }
        widgets = {
            'nombre_categoria': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el nombre de la categoría'
            })
        }
#### ---------------------------------------Tipo Motor--------------------------------------- ####

from django import forms
from .models import TipoMotor

class TipoMotorForm(forms.ModelForm):
    class Meta:
        model = TipoMotor
        fields = ['tipo_motor']
        labels = {
            'tipo_motor': 'Tipo de Motor',
        }
        widgets = {
            'tipo_motor': forms.Select(attrs={'class': 'form-control'}),
        }

#### ---------------------------------------Productos--------------------------------------- ####

from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [
            'nombre_producto',
            'marca',
            'categoria',
            'tipo_motor',
            'descripcion',
            'imagen_url',
            'qr_code',
            'precio',
            'stock'
        ]
        labels = {
            'nombre_producto': 'Nombre del Producto',
            'marca': 'Marca',
            'categoria': 'Categoría',
            'tipo_motor': 'Tipo de Motor',
            'descripcion': 'Descripción',
            'imagen_url': 'URL de la Imagen',
            'qr_code': 'Código QR',
            'precio': 'Precio',
            'stock': 'Stock'
        }
        widgets = {
            'nombre_producto': forms.TextInput(attrs={'placeholder': 'Ingrese el nombre del producto'}),
            'marca': forms.Select(attrs={'class': 'form-select'}),
            'categoria': forms.Select(attrs={'class': 'form-select'}),
            'tipo_motor': forms.Select(attrs={'class': 'form-select'}),
            'descripcion': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Describa el producto'}),
            'imagen_url': forms.URLInput(attrs={'placeholder': 'https://example.com/imagen.jpg'}),
            'qr_code': forms.TextInput(attrs={'placeholder': 'Código QR (opcional)'}),
            'precio': forms.NumberInput(attrs={'step': '0.01', 'placeholder': '0.00'}),
            'stock': forms.NumberInput(attrs={'min': '0', 'placeholder': 'Cantidad en stock'})
        }


#### --------------------------------------- TipoProducto--------------------------------------- ####





from django import forms
from .models import TipoProducto

class TipoProductoForm(forms.ModelForm):
    class Meta:
        model = TipoProducto
        fields = ['nombre_tipo_producto']
        widgets = {
            'nombre_tipo_producto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre del tipo de producto'})
        }


#### --------------------------------------- productos Tipo--------------------------------------- ####

from django import forms
from .models import ProductoTipo, Producto, TipoProducto

class ProductoTipoForm(forms.ModelForm):
    # Selección del Producto con una lista desplegable
    producto = forms.ModelChoiceField(
        queryset=Producto.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Selecciona el Producto",
        required=True
    )
    
    # Selección del Tipo de Producto con una lista desplegable
    tipo_producto = forms.ModelChoiceField(
        queryset=TipoProducto.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Selecciona el Tipo de Producto",
        required=True
    )

    class Meta:
        model = ProductoTipo
        fields = ['producto', 'tipo_producto']
        # Si deseas personalizar los widgets o la presentación de los campos, puedes hacerlo aquí

    def __init__(self, *args, **kwargs):
        super(ProductoTipoForm, self).__init__(*args, **kwargs)
        # Agregar un placeholder y clase CSS adicional para mejorar la apariencia
        self.fields['producto'].widget.attrs.update({'placeholder': 'Selecciona un producto', 'class': 'form-control'})
        self.fields['tipo_producto'].widget.attrs.update({'placeholder': 'Selecciona un tipo de producto', 'class': 'form-control'})

    # Mejorar la experiencia con validaciones si es necesario
    def clean(self):
        cleaned_data = super().clean()
        producto = cleaned_data.get('producto')
        tipo_producto = cleaned_data.get('tipo_producto')

        if producto == tipo_producto:
            raise forms.ValidationError('El producto y el tipo de producto no pueden ser el mismo.')
        
        return cleaned_data


#### ---------------------------------------Clientes--------------------------------------- ####

from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre_cliente', 'contacto_cliente', 'telefono_cliente', 'email_cliente', 
                  'direccion_cliente', 'ruc_cliente']

    # Opcional: puedes personalizar la apariencia de los campos
    nombre_cliente = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del cliente'}))
    contacto_cliente = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contacto del cliente'}), required=False)
    telefono_cliente = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono del cliente'}), required=False)
    email_cliente = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo electrónico del cliente'}), required=False)
    direccion_cliente = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección del cliente'}), required=False)
    ruc_cliente = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'RUC del cliente'}), required=False)



#### ---------------------------------------Proveedores--------------------------------------- ####

from django import forms
from .models import Proveedor

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre_proveedor', 'contacto', 'telefono', 'email', 'direccion']
        widgets = {
            'nombre_proveedor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del proveedor'}),
            'contacto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contacto'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo electrónico'}),
            'direccion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Dirección', 'rows': 3}),
        }

    # Si necesitas validación adicional, puedes agregar métodos aquí.
    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        if telefono and not telefono.isdigit():
            raise forms.ValidationError('El teléfono debe contener solo números.')
        return telefono

#### ---------------------------------------Compra--------------------------------------- ####
from django import forms
from .models import Compra

class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ['proveedor', 'total_compra']  # Campos que aparecerán en el formulario
        widgets = {
            'proveedor': forms.Select(attrs={'class': 'form-control'}),
            'total_compra': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }

    # Se pueden agregar validaciones personalizadas aquí si es necesario
    def clean_total_compra(self):
        total = self.cleaned_data['total_compra']
        if total <= 0:
            raise forms.ValidationError('El total de la compra debe ser mayor a 0.')
        return total


#### -                                       Detalle Compra
# Formulario para DetalleCompra

from django import forms
from .models import DetalleCompra

# Formulario para DetalleCompra
class DetalleCompraForm(forms.ModelForm):
    class Meta:
        model = DetalleCompra
        fields = ['compra', 'producto', 'cantidad', 'precio_unitario']  # Campos que aparecerán en el formulario
        widgets = {
            'compra': forms.Select(attrs={'class': 'form-control'}),
            'producto': forms.Select(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'precio_unitario': forms.NumberInput(attrs={'class': 'form-control'}),
        }

        

#### -                                       ventas

from django import forms
from .models import Venta, DetalleVenta

# Formulario para Venta
class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['cliente', 'tipo_documento', 'numero_documento', 'cliente_nombre', 'cliente_contacto', 'total_venta']
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-control'}),
            'tipo_documento': forms.Select(attrs={'class': 'form-control'}),
            'numero_documento': forms.TextInput(attrs={'class': 'form-control'}),
            'cliente_nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'cliente_contacto': forms.TextInput(attrs={'class': 'form-control'}),
            'total_venta': forms.NumberInput(attrs={'class': 'form-control'}),
        }

# ccc                                    Formulario para DetalleVenta
class DetalleVentaForm(forms.ModelForm):
    class Meta:
        model = DetalleVenta
        fields = ['producto', 'cantidad', 'precio_unitario']
        widgets = {
            'producto': forms.Select(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'precio_unitario': forms.NumberInput(attrs={'class': 'form-control'}),
        }


###                                               tipo document

from django import forms
from .models import TipoDocumento

class TipoDocumentoForm(forms.ModelForm):
    class Meta:
        model = TipoDocumento
        fields = ['tipo_documento']
        widgets = {
            'tipo_documento': forms.Select(attrs={'class': 'form-control'}),
        }
