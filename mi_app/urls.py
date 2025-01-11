from django.urls import path
from . import views




urlpatterns = [
    path("", views.home, name="home"),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    #### marcas ####
    path('marcas/', views.listar_marcas, name='listar_marcas'),
    path('marcas/crear/', views.crear_marca, name='crear_marca'),
    path('marcas/actualizar/<int:pk>/', views.actualizar_marca, name='actualizar_marca'),
    path('marcas/eliminar/<int:pk>/', views.eliminar_marca, name='eliminar_marca'),



    path('categorias/', views.listar_categorias, name='listar_categorias'),
    path('categorias/nueva/', views.crear_categoria, name='crear_categoria'),
    path('categorias/editar/<int:pk>/', views.actualizar_categoria, name='actualizar_categoria'),
    path('categorias/eliminar/<int:pk>/', views.eliminar_categoria, name='eliminar_categoria'),


    path('tipomotor/', views.listar_tipos_motor, name='listar_tipos_motor'),
    path('tipomotor/nuevo/', views.crear_tipo_motor, name='crear_tipo_motor'),
    path('tipomotor/editar/<int:pk>/', views.editar_tipo_motor, name='editar_tipo_motor'),
    path('tipomotor/eliminar/<int:pk>/', views.eliminar_tipo_motor, name='eliminar_tipo_motor'),


    path('productos/', views.listar_productos, name='listar_productos'),
    path('productos/nuevo/', views.crear_producto, name='crear_producto'),
    path('productos/editar/<int:pk>/', views.editar_producto, name='editar_producto'),
    path('productos/eliminar/<int:pk>/', views.eliminar_producto, name='eliminar_producto'),

    path('tipo-productos/', views.tipo_producto_list, name='tipo_productos_listar'),  # Lista de tipos de productos
    path('tipo-productos/nuevo/', views.tipo_producto_create, name='tipo_productos_crear'),  # Crear nuevo tipo de producto
    path('tipo-productos/editar/<int:pk>/', views.tipo_producto_edit, name='tipo_productos_editar'),  # Editar tipo de producto
    path('tipo-productos/eliminar/<int:pk>/', views.tipo_producto_delete, name='tipo_productos_eliminar'),  # Eliminar tipo de producto

        # Lista de relaciones Producto-Tipo Producto
    path('producto-tipo/', views.producto_tipo_list, name='producto_tipo_list'),
    
    # Crear una nueva relación Producto-Tipo Producto
    path('producto-tipo/crear/', views.producto_tipo_create, name='producto_tipo_create'),
    
    # Editar una relación Producto-Tipo Producto existente
    path('producto-tipo/editar/<int:pk>/', views.producto_tipo_edit, name='producto_tipo_edit'),
    
    # Eliminar una relación Producto-Tipo Producto
    path('producto-tipo/eliminar/<int:pk>/', views.producto_tipo_delete, name='producto_tipo_delete'),

    path('productos/detalle/<int:pk>/', views.detalle_producto, name='detalle_producto'),  # Nueva URL



    path('clientes/', views.listar_clientes, name='listar_clientes'),
    path('crear/', views.crear_cliente, name='crear_cliente'),
    path('editar/<int:cliente_id>/', views.editar_cliente, name='editar_cliente'),
    path('eliminar/<int:cliente_id>/', views.eliminar_cliente, name='eliminar_cliente'),



    path('proveedores/', views.listar_proveedores, name='listar_proveedores'),
    path('proveedores/crear/', views.crear_proveedor, name='crear_proveedor'),
    path('proveedores/editar/<int:proveedor_id>/', views.editar_proveedor, name='editar_proveedor'),
    path('proveedores/eliminar/<int:proveedor_id>/', views.eliminar_proveedor, name='eliminar_proveedor'),






    # Listar las compras
    path('compras/', views.listar_compras, name='listar_compras'),

    # Crear una nueva compra
    path('compras/crear/', views.crear_compra, name='crear_compra'),

    # Editar una compra existente
    path('compras/editar/<int:compra_id>/', views.editar_compra, name='editar_compra'),

    # Eliminar una compra
    path('compras/eliminar/<int:compra_id>/', views.eliminar_compra, name='eliminar_compra'),



    # Listar detalles de una compra específica
    path('decompras/<int:compra_id>/detalles/', views.listar_detalles, name='listar_detalles'),
    
    # Agregar detalle de compra
    path('decompras/<int:compra_id>/detalles/agregar/', views.agregar_detalle, name='agregar_detalle'),
    
    # Editar detalle de compra
    path('decompras/<int:compra_id>/detalles/editar/<int:detalle_id>/', views.editar_detalle, name='editar_detalle'),
    
    # Eliminar detalle de compra
    path('decompras/<int:compra_id>/detalles/eliminar/<int:detalle_id>/', views.eliminar_detalle, name='eliminar_detalle'),





    path('ventas/', views.listar_ventas, name='listar_ventas'),
    path('ventas/nueva/', views.crear_venta, name='crear_venta'),
    path('ventas/editar/<int:venta_id>/', views.editar_venta, name='editar_venta'),
    path('ventas/eliminar/<int:venta_id>/', views.eliminar_venta, name='eliminar_venta'),
    #path('ventas/detalle/<int:venta_id>/', views.agregar_detalle_venta, name='agregar_detalle_venta')


    path('ventas/<int:venta_id>/detalles/', views.listar_detalles_venta, name='listar_detalles_venta'),
    path('ventas/<int:venta_id>/detalles/agregar/', views.agregar_detalle_venta, name='agregar_detalle_venta'),
    path('ventas/detalles/editar/<int:detalle_id>/', views.editar_detalle_venta, name='editar_detalle_venta'),
    path('ventas/detalles/eliminar/<int:detalle_id>/', views.eliminar_detalle_venta, name='eliminar_detalle_venta'),





    path('tipos-documento/', views.listar_tipos_documento, name='listar_tipos_documento'),
    path('tipos-documento/nuevo/', views.crear_tipo_documento, name='crear_tipo_documento'),
    path('tipos-documento/editar/<int:pk>/', views.editar_tipo_documento, name='editar_tipo_documento'),
    path('tipos-documento/eliminar/<int:pk>/', views.eliminar_tipo_documento, name='eliminar_tipo_documento'),





    path('calculadora/', views.calculadora, name='calculadora'),
]



