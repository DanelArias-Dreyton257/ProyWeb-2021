from django import forms

# Clase Pedido con telefono, direccion, listado de pizzas y nombre del cliente
class Pedido(forms.Form):

    email = forms.EmailField()
    nombre = forms.CharField()
    apellido = forms.CharField()
    calle = forms.CharField()
    cPostal = forms.IntegerField()
    nTelefono = forms.CharField()
    precio = forms.FloatField()

    def __str__(self):
        return "{} | {} ({}€ -- {})".format(self.email, self.nombre, self.precio, self.calle)
