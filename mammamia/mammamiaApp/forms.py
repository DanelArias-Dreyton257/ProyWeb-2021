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

    email.widget.attrs.update({'class': 'form-control', 'placeholder' : 'example@mail.com'})
    nombre.widget.attrs.update({'class': 'form-control', 'placeholder' : 'Name'})
    apellido.widget.attrs.update({'class': 'form-control', 'placeholder' : 'Surname'})
    calle.widget.attrs.update({'class': 'form-control', 'placeholder' : 'Address'})
    cPostal.widget.attrs.update({'class': 'form-control', 'placeholder' : 10010})
    nTelefono.widget.attrs.update({'class': 'form-control', 'placeholder' : '699999999'})
    precio.widget.attrs.update({'class': 'form-control', 'placeholder' : 22.98})

    def __str__(self):
        return "{} | {} ({}€ -- {})".format(self.email, self.nombre, self.precio, self.calle)
