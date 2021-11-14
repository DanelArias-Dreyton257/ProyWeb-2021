from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Pizza, Masa, Ingrediente

# Create your views here.

# Esta funcion mostrara una portada, la cual, aparecera una lista de masas, con una pizza por cada masa
def portada(request):
    lista_m = get_list_or_404(Masa)

    lista_min_p = []
    for masa in lista_m: #Busca las pizzas mas baratas de cada masa
        lista_min_p.append(min(masa.pizza_set.all()))

    context = {
       'lista_min_p' : lista_min_p,
    }
    return render(request,'portada.html', context)

# Esta funcion mostrara un listado de todas las pizzas
def listaPizzas(request):
    lista = get_list_or_404(Pizza.objects.all().order_by('nombre'))
    context = {
        'lista_pizzas': lista,
    }
    return render(request,'listaPizzas.html', context)

# Esta funcion mostrara un listado de todas las masas
def listaMasas(request):
    lista = get_list_or_404(Masa.objects.all().order_by('nombre'))
    context = {
        'lista_masas': lista,
    }
    return render(request,'listaMasas.html', context)

# Esta funcion mostrara un listado de todos los ingredientes
def listaIngredientes(request):
    lista = get_list_or_404(Ingrediente.objects.all().order_by('nombre'))
    context = {
        'lista_ingredientes': lista,
    }
    return render(request,'listaIngredientes.html', context)

# Esta funcion mostrara todos los detalles de la pizza
def detallePizza(request, id_pizza):
    pizza = get_object_or_404(Pizza, pk=id_pizza)

    context = {
        'pizza' :pizza,
    }
    return render(request,'detallePizza.html', context)

# Esta funcion mostrara todos los detalles de la masa
def detalleMasa(request, id_masa):
    masa = get_object_or_404(Masa, pk=id_masa)

    context = {
        'masa' :masa,
    }
    return render(request,'detalleMasa.html', context)

# Esta funcion mostrara todos los detalles de los ingredientes
def detalleIngrediente(request, id_ingrediente):
    ingrediente = get_object_or_404(Ingrediente, pk=id_ingrediente)

    context = {
        'ingrediente' :ingrediente,
    }
    return render(request,'detalleIngrediente.html', context)
