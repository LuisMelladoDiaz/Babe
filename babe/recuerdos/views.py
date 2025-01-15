from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Recuerdo
from .forms import RecuerdoForm, ArchivoRecuerdoFormSet
from django.views.generic import ListView, DeleteView
from django.db import transaction

# Listado de recuerdos
class RecuerdoListView(ListView):
    model = Recuerdo
    template_name = 'lista_recuerdos.html'
    context_object_name = 'recuerdos'

# Crear recuerdo con archivos
def crear_recuerdo(request):
    if request.method == "POST":
        form = RecuerdoForm(request.POST)
        formset = ArchivoRecuerdoFormSet(request.POST, request.FILES)
        if form.is_valid() and formset.is_valid():
            with transaction.atomic():
                recuerdo = form.save()
                formset.instance = recuerdo
                formset.save()
            return redirect('lista_recuerdos')
    else:
        form = RecuerdoForm()
        formset = ArchivoRecuerdoFormSet()
    return render(request, 'formulario_recuerdo.html', {'form': form, 'formset': formset})

# Editar recuerdo con archivos
def editar_recuerdo(request, pk):
    recuerdo = Recuerdo.objects.get(pk=pk)
    if request.method == "POST":
        form = RecuerdoForm(request.POST, instance=recuerdo)
        formset = ArchivoRecuerdoFormSet(request.POST, request.FILES, instance=recuerdo)
        if form.is_valid() and formset.is_valid():
            with transaction.atomic():
                form.save()
                formset.save()
            return redirect('lista_recuerdos')
    else:
        form = RecuerdoForm(instance=recuerdo)
        formset = ArchivoRecuerdoFormSet(instance=recuerdo)
    return render(request, 'formulario_recuerdo.html', {'form': form, 'formset': formset})

# Eliminar recuerdo
class RecuerdoDeleteView(DeleteView):
    model = Recuerdo
    template_name = 'confirmar_eliminar.html'
    success_url = reverse_lazy('lista_recuerdos')
