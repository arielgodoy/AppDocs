# urls.py
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.ListarPropiedadesView.as_view(), name='listar_propiedades'),  # Redirigir a la lista de propiedades
    path('propiedades/<int:pk>/', views.DetallePropiedadView.as_view(), name='detalle_propiedad'),
    path('propiedades/<int:pk>/crear_documento/', views.CrearDocumentoView.as_view(), name='crear_documento'),
    path('documentos/<int:pk>/eliminar/', views.eliminar_documento, name='eliminar_documento'),    
    path('ingresar_propietario/', views.CrearPropietarioView.as_view(), name='crear_propietario'),
    path('listar_propietarios/', views.ListarPropietariosView.as_view(), name='listar_propietarios'),
    path('propietarios/<int:pk>/', views.DetallePropietarioView.as_view(), name='detalle_propietario'),
    path('propietarios/<int:pk>/eliminar/', views.EliminarPropietarioView.as_view(), name='eliminar_propietario'),
    path('propietarios/<int:pk>/modificar/', views.ModificarPropietarioView.as_view(), name='modificar_propietario'),

    path('ingresar_propiedad/', views.CrearPropiedadView.as_view(), name='crear_propiedad'),
    path('propiedades/<int:pk>/eliminar/', views.EliminarPropiedadView.as_view(), name='eliminar_propiedad'),
    path('propiedades/<int:pk>/modificar/', views.ModificarPropiedadView.as_view(), name='modificar_propiedad'),


    path('crear_tipo_documento/', views.CrearTipoDocumentoView.as_view(), name='crear_tipo_documento'),
    path('listar_tipos_documentos/', views.ListarTiposDocumentosView.as_view(), name='listar_tipos_documentos'),
    path('modificar_tipo_documento/<int:pk>/', views.ModificarTipoDocumentoView.as_view(), name='modificar_tipo_documento'),
    path('eliminar_tipo_documento/<int:pk>/', views.EliminarTipoDocumentoView.as_view(), name='eliminar_tipo_documento'),




    path('conversaciones/', views.lista_conversaciones, name='lista_conversaciones'),
    path('conversaciones/<int:conversacion_id>/enviar-mensaje/', views.enviar_mensaje, name='enviar_mensaje'),
    path('conversaciones/crear/', views.crear_conversacion, name='crear_conversacion'),
    path('conversaciones/<int:conversacion_id>/', views.detalle_conversacion, name='detalle_conversacion'),
    path('conversacion/<int:conversacion_id>/eliminar/', views.eliminar_conversacion, name='eliminar_conversacion'),


    

    
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registro/', views.registro_usuario, name='registro_usuario'),    
    path('subeavatar', views.subeAvatar, name='subeavatar'),
    path('cambiar-password/', views.cambiar_password, name='cambiar_password'),
    path('about/', views.about, name='about'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)