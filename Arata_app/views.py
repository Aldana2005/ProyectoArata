from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Semilla
from .forms import SemillaForm
def inicio(request):
    return render(request, 'base.html')

def sobre_nosotros(request):
    return render(request, 'sobre_nosotros.html')

def servicios(request):
    semillas = Semilla.objects.all()
    return render(request, 'servicios.html', {'semillas': semillas})

def contacto(request):
    return render(request, 'contacto.html')
def home(request):
    # Calcular las cantidades
    total_semillas = Semilla.objects.count()
    

    # Pasar las cantidades al contexto
    context = {'total_semillas': total_semillas}

    # Renderizar la plantilla con el contexto
    return render(request, 'semillas/base_semilla.html', context)

def semilla_list(request):
    semillas = Semilla.objects.all()

    # Configurar paginación
    paginator = Paginator(semillas, 10)  # Mostrar 10 semillas por página
    page = request.GET.get('page')

    try:
        semillas_paginadas = paginator.page(page)
    except PageNotAnInteger:
        semillas_paginadas = paginator.page(1)
    except EmptyPage:
        semillas_paginadas = paginator.page(paginator.num_pages)

    return render(request, 'semillas/semilla_list.html', {'semillas': semillas_paginadas})



def semilla_new(request):
   
    if request.method == "POST":
        form = SemillaForm(request.POST, request.FILES)
        if form.is_valid():
            semilla = form.save()
            return redirect('semilla_list')
        else:
            print(form.errors)
    else:
        form = SemillaForm()

    return render(request, 'semillas/semilla_edit.html', {'form': form})




def semilla_edit(request, pk):
    semilla = get_object_or_404(Semilla, pk=pk)
   
    if request.method == "POST":
        form = SemillaForm(request.POST, request.FILES, instance=semilla)
        if form.is_valid():
            form.save()
            print("Semilla guardada exitosamente")
            return redirect('semilla_list')
        else:
            print("Errores en el formulario:", form.errors)
    else:
        form = SemillaForm(instance=semilla)

    return render(request, 'semillas/semilla_edit.html', {'form': form})


def semilla_delete(request, pk):
    semilla = get_object_or_404(Semilla, pk=pk)
    semilla.delete()
    return redirect('semilla_list')

