from django.urls import path

from . import views

urlpatterns = [

#--------------------PRUEBA--------------------
    path('', views.index, name="index"),
#--------------------PRUEBA--------------------

]
