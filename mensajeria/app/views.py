from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import CreateView, UpdateView, ListView
from django.core.urlresolvers import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from .models import Servicio, Status, Notificador
from .forms import ServicioForm, AusenciaForm

def listing(request):
    lista_servicios = Servicio.objects.filter(fechaFin__isnull=True)
    paginator = Paginator(lista_servicios, 8, orphans=3) 

    page = request.GET.get('page')
    try:
        servicios = paginator.page(page)
    except PageNotAnInteger:
        servicios = paginator.page(1)
    except EmptyPage:
        servicios = paginator.page(paginator.num_pages)
    return render(request, 'index.html', {"servicios": servicios})

class ServiciosForm(CreateView):
    model = Servicio
    template_name = 'servicios.html'
    form_class = ServicioForm
    success_url = reverse_lazy('notificadores')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ServiciosForm, self).dispatch(*args, **kwargs)  


    def form_valid(self, form):
        self.servicio = form.save(commit=False)

        form.instance.solicitante = self.request.user
        self.servicio.notificador = form.cleaned_data['notificador']
        self.servicio.sitio = form.cleaned_data['sitio']
        self.servicio.actividad = form.cleaned_data['actividad']
        self.servicio.comentarios = form.cleaned_data['comentarios']
        self.servicio.save()
        self.servicio.notificador.statusNotificador = Status.objects.get(id = 2)#Status No Disponible
        self.servicio.notificador.save()
        return super(ServiciosForm, self).form_valid(form)

import datetime

def enterado(request, id_servicio):
    enterado = Servicio.objects.get(id=id_servicio)
    enterado.fechaEnterado = datetime.datetime.now()
    enterado.save()
    return HttpResponseRedirect("/")

def finalizar(request, id_servicio):
    finalizar = Servicio.objects.get(id=id_servicio)
    finalizar.fechaFin = datetime.datetime.now()
    finalizar.save()
    if finalizar.fechaFin:
        finalizar.notificador.statusNotificador = Status.objects.get(id = 1)#Status Disponible
        finalizar.notificador.save()
    return HttpResponseRedirect("/pendientes/")

@login_required(login_url='/ingresar/')
def pendientes(request):
    solicitante1 = request.user
    lista_servicios = Servicio.objects.filter(fechaFin__isnull=True, solicitante = solicitante1)
    paginator = Paginator(lista_servicios, 8, orphans=3) # Show 8 contacts per page

    page = request.GET.get('page')
    try:
        servicios = paginator.page(page)
    except PageNotAnInteger:
        servicios = paginator.page(1)
    except EmptyPage:
        servicios = paginator.page(paginator.num_pages)

    return render(request, 'pendientes.html', {"servicios": servicios})

class NotificadorList(ListView):
      model = Notificador
      template_name = 'lista-notificadores.html'
      context_object_name = 'notificadores'

class NotificadorUpdate(UpdateView):
    model =Notificador
    template_name="ausencias.html"
    form_class = AusenciaForm
    success_url = reverse_lazy('listNoti')

def listingTable(request):
    lista_servicios = Servicio.objects.filter(fechaFin__isnull=True)
    paginator = Paginator(lista_servicios, 8, orphans=3) 

    page = request.GET.get('page')
    try:
        servicios = paginator.page(page)
    except PageNotAnInteger:
        servicios = paginator.page(1)
    except EmptyPage:
        servicios = paginator.page(paginator.num_pages)
    return render(request, 'table.html', {"servicios": servicios})
