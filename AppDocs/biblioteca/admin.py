from django.contrib import admin
from .models import TipoDocumento,Propietario,Propiedad,Documento,Conversacion, Mensaje
# Register your models here.

admin.site.register(TipoDocumento)
admin.site.register(Propietario)
admin.site.register(Propiedad)
admin.site.register(Conversacion)
admin.site.register(Mensaje)

#admin.site.register(MiUsuario)