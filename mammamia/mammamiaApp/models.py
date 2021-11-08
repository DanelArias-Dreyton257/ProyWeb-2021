from django.db import models

# Create your models here.

class Masa(models.Model):
    nombre = models.CharField(max_length=50)
    grosormm = models.IntegerField()
    tipoHarina = models.CharField(max_length=50)
    supPrecio = models.DecimalField(decimal_places=2, default=0, max_digits=4)

    def __str__(self):
        return "{} (+{}€)".format(self.nombre, self.supPrecio)

class Ingrediente(models.Model):
    nombre = models.CharField(max_length=50)
    origen = models.CharField(max_length=50)
    kcal = models.DecimalField(decimal_places=2, default=0, max_digits=7)

    #Falta pizzas -Mirar como hacer tablas n a m

    def __str__(self):
        return "{}".format(self.nombre)

class Pizza(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(decimal_places=2, default=0, max_digits=5)
    masa = models.ForeignKey(Masa, on_delete=models.CASCADE)

    ingredientes = models.ManyToManyField(Ingrediente, related_name='pizzas')
    #Falta ingredientes -Mirar como hacer tablas n a m

    def __str__(self):
        return "{} ({}€)".format(self.nombre, self.precio)
