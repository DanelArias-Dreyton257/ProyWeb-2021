from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import *
from django.views.generic import *
from django.core.mail import send_mail, send_mass_mail
from mammamia.settings import EMAIL_HOST_USER


# Vistas basadas en funciones

# Esta funcion mostrara una portada, la cual, aparecera una lista de masas, con una pizza por cada masa
# def portada(request):
#     lista_m = get_list_or_404(Masa)
#
#     lista_min_p = []
#     for masa in lista_m: #Busca las pizzas mas baratas de cada masa
#         lista_min_p.append(min(masa.pizza_set.all()))
#
#     context = {
#        'lista_min_p' : lista_min_p,
#     }
#     return render(request,'portada.html', context)
#
# Esta funcion mostrara un listado de todas las pizzas
# def listaPizzas(request):
#     lista = get_list_or_404(Pizza.objects.all().order_by('nombre'))
#     context = {
#         'lista_pizzas': lista,
#     }
#     return render(request,'listaPizzas.html', context)
#
# Esta funcion mostrara un listado de todas las masas
# def listaMasas(request):
#     lista = get_list_or_404(Masa.objects.all().order_by('nombre'))
#     context = {
#         'lista_masas': lista,
#     }
#     return render(request,'listaMasas.html', context)
#
# Esta funcion mostrara un listado de todos los ingredientes
# def listaIngredientes(request):
#     lista = get_list_or_404(Ingrediente.objects.all().order_by('nombre'))
#     context = {
#         'lista_ingredientes': lista,
#     }
#     return render(request,'listaIngredientes.html', context)
#
# Esta funcion mostrara todos los detalles de la pizza
# def detallePizza(request, id_pizza):
#     pizza = get_object_or_404(Pizza, pk=id_pizza)
#
#     context = {
#         'pizza' :pizza,
#     }
#     return render(request,'detallePizza.html', context)
#
# Esta funcion mostrara todos los detalles de la masa
# def detalleMasa(request, id_masa):
#     masa = get_object_or_404(Masa, pk=id_masa)
#
#     context = {
#         'masa' :masa,
#     }
#     return render(request,'detalleMasa.html', context)
#
# Esta funcion mostrara todos los detalles de los ingredientes
# def detalleIngrediente(request, id_ingrediente):
#     ingrediente = get_object_or_404(Ingrediente, pk=id_ingrediente)
#
#     context = {
#         'ingrediente' :ingrediente,
#     }
#     return render(request,'detalleIngrediente.html', context)
#
# Vistas basadas en clases

# Esta funcion mostrara una portada, la cual, aparecera una lista de masas, con una pizza por cada masa
class Portada(ListView):
    model = Masa
    lista_min_p = []
    lista_m = get_list_or_404(Masa)
    for masa in lista_m: #Busca las pizzas mas baratas de cada masa
        lista_min_p.append(min(masa.pizza_set.all()))
    queryset = lista_min_p
    template_name = "portada.html"
    context_object_name = "lista_min_p"

# Esta funcion mostrara un listado de todas las pizzas
class ListaPizzas(ListView):
    model = Pizza
    lista = get_list_or_404(Pizza)
    queryset = lista
    template_name = "listaPizzas.html"
    context_object_name = "lista_pizzas"

# Esta funcion mostrara un listado de todas las masas
class ListaMasas(ListView):
    model = Masa
    lista = get_list_or_404(Masa.objects.all().order_by('nombre'))
    queryset = lista
    template_name = "listaMasas.html"
    context_object_name = "lista_masas"

# Esta funcion mostrara un listado de todos los ingredientes
class ListaIngredientes(ListView):
    model = Ingrediente
    lista = get_list_or_404(Ingrediente.objects.all().order_by('nombre'))
    queryset = lista
    template_name = "listaIngredientes.html"
    context_object_name = "lista_ingredientes"

# Esta funcion mostrara todos los detalles de la pizza
class DetallePizza(DetailView):
    model = Pizza
    template_name = "detallePizza.html"
    context_object_name = "pizza"


# Esta funcion mostrara todos los detalles de la masa
class DetalleMasa(DetailView):
    model = Masa
    template_name = "detalleMasa.html"
    context_object_name = "masa"

# Esta funcion mostrara todos los detalles de los ingredientes
class DetalleIngrediente(DetailView):
    model = Ingrediente
    template_name = "detalleIngrediente.html"
    context_object_name = "ingrediente"


def calcularPrecio(post):
    lista_p = get_list_or_404(Pizza)

    #for (pizza in lista_p):


    return 100

def correoUsuario(post):

    subject = 'Tu pedido en MammaMia ha sido recibido'
    precio=calcularPrecio(post)
    message = 'Hola {} {}.\nTu pedido se ha recibido correctamente.\nHa costado: {}€\nSe le enviarán el {} a esta dirección: {} con cod.postal: {}\nSi hay cualquier problema se le contactará a este mismo correo.'.format(
        post.get('contact_name',''),
        post.get('contact_surname',''),
        str(precio),
        str(post.get('hyt','')), #faltaria formatear la hora
        post.get('contact_street',''),
        str(post.get('contact_pCode',''))
    )
    recepient = post.get('contact_email','')

    dir = {
        'subject':subject,
        'message': message,
        'recepient': recepient
    }

    return dir

def correoEmpresa(post):
    subject='A order has been placed'
    message='This a test message for myself'
    recepient = EMAIL_HOST_USER

    dir = {
        'subject':subject,
        'message': message,
        'recepient': recepient
    }

    return dir

def pedido(request):

    lista_p = get_list_or_404(Pizza)
    #form
    if request.method == 'POST':

        dirU = correoUsuario(request.POST)
        dirE = correoEmpresa(request.POST)

        datatuple = (
            (dirU['subject'], dirU['message'], EMAIL_HOST_USER, [dirU['recepient']]),
            (dirE['subject'], dirE['message'], EMAIL_HOST_USER, [dirE['recepient']]),
        )

        send_mass_mail(datatuple, fail_silently = False)

        return render(request, 'success.html', {'recepient': dirU['recepient']})

    context = {
        'lista_p': lista_p,
    }

    return render(request,'pedido.html',context)
