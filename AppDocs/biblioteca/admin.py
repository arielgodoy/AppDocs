from django.contrib import admin
from .models import TipoDocumento,Propietario,Propiedad,Documento,Conversacion, Mensaje,Avatar
# Register your models here.

admin.site.register(TipoDocumento)
admin.site.register(Propietario)
admin.site.register(Propiedad)
admin.site.register(Conversacion)
admin.site.register(Mensaje)
admin.site.register(Avatar)


#admin.site.register(MiUsuario)