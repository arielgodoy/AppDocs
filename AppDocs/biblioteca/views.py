# views.py
from django.views.generic.edit import UpdateView
from django.shortcuts import render, redirect,get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from .models import Propiedad, Documento,Propietario
from .forms import DocumentoForm,PropietarioForm,PropiedadForm
from django.urls import reverse
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from .models import TipoDocumento
from .forms import TipoDocumentoForm
from django.views.generic import View


def vista_login(request):
    return LoginView.as_view(template_name='login.html')(request)


class ListarPropiedadesView(ListView):    
    model = Propiedad
    template_name = 'listar_propiedades.html'
    context_object_name = 'propiedades'

class DetallePropiedadView(DetailView):
    model = Propiedad
    template_name = 'detalle_propiedad.html'
    context_object_name = 'propiedad'

class CrearDocumentoView(CreateView):
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




class CrearPropietarioView(CreateView):
    model = Propietario
    form_class = PropietarioForm
    template_name = 'crear_propietario.html'
    success_url = reverse_lazy('crear_propietario')


class ListarPropietariosView(ListView):    
    model = Propietario
    template_name = 'listar_propietarios.html'
    context_object_name = 'propietarios'

class DetallePropietarioView(DetailView):
    model = Propietario
    template_name = 'detalle_propietario.html'
    context_object_name = 'propietario'

class EliminarPropietarioView(DeleteView):
    model = Propietario
    template_name = 'eliminar_propietario.html'
    success_url = reverse_lazy('listar_propietarios')
class ModificarPropietarioView(UpdateView):
    model = Propietario
    form_class = PropietarioForm
    template_name = 'modificar_propietario.html'
    success_url = reverse_lazy('listar_propietarios')
    # No es necesario el método form_valid
    # ...

class CrearPropiedadView(CreateView):
    model = Propiedad
    form_class = PropiedadForm
    template_name = 'crear_propiedad.html'
    success_url = reverse_lazy('crear_propiedad')


class EliminarPropiedadView(DeleteView):
    model = Propiedad
    template_name = 'eliminar_propiedad.html'
    success_url = reverse_lazy('listar_propiedades')

    def form_valid(self, form):
        # Obtener la propiedad a eliminar
        propiedad = self.get_object()
        # Eliminar la propiedad
        propiedad.delete()
        return redirect(self.success_url)


class ModificarPropiedadView(UpdateView):
    model = Propiedad
    form_class = PropiedadForm
    template_name = 'modificar_propiedad.html'
    success_url = reverse_lazy('listar_propiedades')

    def form_valid(self, form):
        # Guardar los cambios en la propiedad
        propiedad = form.save()
        return super().form_valid(form)


class CrearTipoDocumentoView(CreateView):
    model = TipoDocumento
    form_class = TipoDocumentoForm
    template_name = 'crear_tipo_documento.html'
    success_url = reverse_lazy('listar_tipos_documentos')

class ListarTiposDocumentosView(ListView):
    model = TipoDocumento
    template_name = 'listar_tipos_documentos.html'
    context_object_name = 'tipos_documentos'






class ModificarTipoDocumentoView(View):
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

class EliminarTipoDocumentoView(View):
    template_name = 'eliminar_tipo_documento.html'
    success_url = reverse_lazy('listar_tipos_documentos')

    def get(self, request, pk):
        tipo_documento = get_object_or_404(TipoDocumento, pk=pk)
        return render(request, self.template_name, {'tipo_documento': tipo_documento})

    def post(self, request, pk):
        tipo_documento = get_object_or_404(TipoDocumento, pk=pk)
        tipo_documento.delete()
        return redirect(self.success_url)
