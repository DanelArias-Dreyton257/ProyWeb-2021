from django.urls import path

from . import views

urlpatterns = [
    #mammamia/home
    path('home', views.portada, name='portada'),

    #mammamia/pizzas
    path('pizzas', views.listaPizzas, name='pizzas'),
    #mammamia/pizzas/[id_pizza]
    path('pizzas/<int:id_pizza>', views.detallePizza,name='detalle_pizza'),

    #mammamia/masas
    path('masas', views.listaMasas, name='masa'),
    #mammamia/masas/[id_masa]
    path('masas/<int:id_masa>', views.detalleMasa, name='detalle_masa'),

    #mammamia/ingredientes
    path('ingredientes', views.listaIngredientes, name='ingredientes'),
    #mammamia/masas/[id_ingrediente]
    path('ingredientes/<int:id_ingrediente>', views.detalleIngrediente, name='detalle_ingrediente'),
]
