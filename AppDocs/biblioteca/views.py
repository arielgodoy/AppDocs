# views.py
from django.views.generic.edit import UpdateView
from django.shortcuts import render, redirect,get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from .models import Propiedad, Documento,Propietario,Conversacion,Mensaje
from .forms import DocumentoForm,PropietarioForm,PropiedadForm
from django.urls import reverse
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from .models import TipoDocumento
from .forms import TipoDocumentoForm
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import MensajeForm,ConversacionForm, EnviarMensajeForm

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('listar_propiedades')  # Redirigir al usuario a la página de inicio después de un login exitoso
        else:
            # Mostrar mensaje de error si el login no es válido
            error_message = "Nombre de usuario o contraseña incorrectos."
            return render(request, 'login.html', {'error_message': error_message})
    return render(request, 'login.html')

def logout_view(request):
    # Vista para realizar el logout (opcional)
    logout(request)
    return redirect('login')





class ListarPropiedadesView(LoginRequiredMixin,ListView):    
    model = Propiedad
    template_name = 'listar_propiedades.html'
    context_object_name = 'propiedades'

class DetallePropiedadView(LoginRequiredMixin,DetailView):
    model = Propiedad
    template_name = 'detalle_propiedad.html'
    context_object_name = 'propiedad'

class CrearDocumentoView(LoginRequiredMixin,CreateView):
    model = Documento
    form_class = DocumentoForm
    template_name = 'crear_documento.html'
    success_url = reverse_lazy('listar_propiedades')

    def form_valid(self, form):
        # Guardar los cambios en la propiedad
        propiedad = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('detalle_propiedad', kwargs={'pk': self.object.propiedad.pk})

def eliminar_documento(request, pk):
    # Obtener el documento a eliminar
    documento = get_object_or_404(Documento, pk=pk)

    # Eliminar el documento
    documento.delete()

    # Redireccionar a la página de detalles de la propiedad
    return redirect('detalle_propiedad', pk=documento.propiedad.pk)




class CrearPropietarioView(LoginRequiredMixin,CreateView):
    model = Propietario
    form_class = PropietarioForm
    template_name = 'crear_propietario.html'
    success_url = reverse_lazy('crear_propietario')


class ListarPropietariosView(LoginRequiredMixin,ListView):    
    model = Propietario
    template_name = 'listar_propietarios.html'
    context_object_name = 'propietarios'

class DetallePropietarioView(LoginRequiredMixin,DetailView):
    model = Propietario
    template_name = 'detalle_propietario.html'
    context_object_name = 'propietario'

class EliminarPropietarioView(LoginRequiredMixin,DeleteView):
    model = Propietario
    template_name = 'eliminar_propietario.html'
    success_url = reverse_lazy('listar_propietarios')
class ModificarPropietarioView(LoginRequiredMixin,UpdateView):
    model = Propietario
    form_class = PropietarioForm
    template_name = 'modificar_propietario.html'
    success_url = reverse_lazy('listar_propietarios')
    # No es necesario el método form_valid
    # ...

class CrearPropiedadView(LoginRequiredMixin,CreateView):
    model = Propiedad
    form_class = PropiedadForm
    template_name = 'crear_propiedad.html'
    success_url = reverse_lazy('crear_propiedad')


class EliminarPropiedadView(LoginRequiredMixin,DeleteView):
    model = Propiedad
    template_name = 'eliminar_propiedad.html'
    success_url = reverse_lazy('listar_propiedades')

    def form_valid(self, form):
        # Obtener la propiedad a eliminar
        propiedad = self.get_object()
        # Eliminar la propiedad
        propiedad.delete()
        return redirect(self.success_url)


class ModificarPropiedadView(LoginRequiredMixin,UpdateView):
    model = Propiedad
    form_class = PropiedadForm
    template_name = 'modificar_propiedad.html'
    success_url = reverse_lazy('listar_propiedades')

    def form_valid(self, form):
        # Guardar los cambios en la propiedad
        propiedad = form.save()
        return super().form_valid(form)


class CrearTipoDocumentoView(LoginRequiredMixin,CreateView):
    model = TipoDocumento
    form_class = TipoDocumentoForm
    template_name = 'crear_tipo_documento.html'
    success_url = reverse_lazy('listar_tipos_documentos')

class ListarTiposDocumentosView(LoginRequiredMixin,ListView):
    model = TipoDocumento
    template_name = 'listar_tipos_documentos.html'
    context_object_name = 'tipos_documentos'






class ModificarTipoDocumentoView(LoginRequiredMixin,View):
    template_name = 'modificar_tipo_documento.html'
    success_url = reverse_lazy('listar_tipos_documentos')

    def get(self, request, pk):
        tipo_documento = get_object_or_404(TipoDocumento, pk=pk)
        form = TipoDocumentoForm(instance=tipo_documento)
        return render(request, self.template_name, {'form': form})

    def post(self, request, pk):
        tipo_documento = get_object_or_404(TipoDocumento, pk=pk)
        form = TipoDocumentoForm(request.POST, instance=tipo_documento)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        return render(request, self.template_name, {'form': form})

class EliminarTipoDocumentoView(LoginRequiredMixin,View):
    template_name = 'eliminar_tipo_documento.html'
    success_url = reverse_lazy('listar_tipos_documentos')

    def get(self, request, pk):
        tipo_documento = get_object_or_404(TipoDocumento, pk=pk)
        return render(request, self.template_name, {'tipo_documento': tipo_documento})

    def post(self, request, pk):
        tipo_documento = get_object_or_404(TipoDocumento, pk=pk)
        tipo_documento.delete()
        return redirect(self.success_url)







@login_required
def lista_conversaciones(request):    
    conversaciones = Conversacion.objects.filter(participantes=request.user)   
    
    print(conversaciones)
    return render(request, 'lista_conversaciones.html', {'conversaciones': conversaciones})

@login_required
def enviar_mensaje(request, conversacion_id):
    conversacion = get_object_or_404(Conversacion, id=conversacion_id, participantes=request.user)
    form = MensajeForm(request.POST or None)
    
    if request.method == 'POST' and form.is_valid():
        mensaje = form.save(commit=False)
        mensaje.conversacion = conversacion
        mensaje.remitente = request.user
        mensaje.save()
        return redirect('detalle_conversacion', conversacion_id=conversacion_id)

    return render(request, 'enviar_mensaje.html', {'conversacion': conversacion, 'form': form})

@login_required
def crear_conversacion(request):
    if request.method == 'POST':
        form = ConversacionForm(request.POST, user=request.user)
        if form.is_valid():
            conversacion = form.save()
            # Imprime el ID de la nueva conversación para verificar que se está generando y guardando correctamente
            print(f"ID de la nueva conversación: {conversacion.id}")
            return redirect('detalle_conversacion', conversacion_id=conversacion.id)
    else:
        form = ConversacionForm(user=request.user)

    return render(request, 'crear_conversacion.html', {'form': form})

@login_required
def detalle_conversacion(request, conversacion_id):
    conversacion = get_object_or_404(Conversacion, id=conversacion_id, participantes=request.user)
    mensajes = Mensaje.objects.filter(conversacion=conversacion)

    if request.method == 'POST':
        form = EnviarMensajeForm(request.POST)
        if form.is_valid():
            mensaje = Mensaje(contenido=form.cleaned_data['contenido'], conversacion=conversacion, remitente=request.user)
            mensaje.save()
            return redirect('detalle_conversacion', conversacion_id=conversacion_id)
    else:
        form = EnviarMensajeForm()

    return render(request, 'detalle_conversacion.html', {'conversacion': conversacion, 'mensajes': mensajes, 'form': form})