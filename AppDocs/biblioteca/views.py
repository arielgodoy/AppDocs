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
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from .models import TipoDocumento
from .forms import TipoDocumentoForm
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages










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
        propiedad = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('detalle_propiedad', kwargs={'pk': self.object.propiedad.pk})

@login_required
def eliminar_documento(request, pk):    
    documento = get_object_or_404(Documento, pk=pk)    
    documento.delete()    
    return redirect('detalle_propiedad', pk=documento.propiedad.pk)




class CrearPropietarioView(LoginRequiredMixin,CreateView):
    model = Propietario
    form_class = PropietarioForm
    template_name = 'crear_propietario.html'
    success_url = reverse_lazy('listar_propietarios')



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

class CrearPropiedadView(LoginRequiredMixin,CreateView):
    model = Propiedad
    form_class = PropiedadForm
    template_name = 'crear_propiedad.html'
    success_url = reverse_lazy('listar_propiedades')


class EliminarPropiedadView(LoginRequiredMixin,DeleteView):
    model = Propiedad
    template_name = 'eliminar_propiedad.html'
    success_url = reverse_lazy('listar_propiedades')

    def form_valid(self, form):        
        propiedad = self.get_object()        
        propiedad.delete()
        return redirect(self.success_url)


class ModificarPropiedadView(LoginRequiredMixin,UpdateView):
    model = Propiedad
    form_class = PropiedadForm
    template_name = 'modificar_propiedad.html'
    success_url = reverse_lazy('listar_propiedades')

    def form_valid(self, form):        
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
def about(request):
    return render(request, 'about.html')




    