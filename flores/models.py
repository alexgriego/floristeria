from django.db import models

# Create your models here.
class Inventario_de_flores(models.Model):
    nombre = models.CharField(max_length=64)
    tipo = models.CharField(max_length=64)
    nit = models.CharField(max_length=64)
    temporada = models.CharField(max_length=64)
    ocasion = models.CharField(max_length=64)
    def __str__(self):
        return self.nombre

class Oferta(models.Model):
    flores_en_descuento = models.ForeignKey(Inventario_de_flores, on_delete=models.PROTECT)
    usuario_con_descuento = models.CharField(max_length=64)
    valor_de_descuento = models.FloatField()
    def __str__(self):
        return str (self.flores_en_descuento)


class Compra(models.Model):
    valor_de_compra = models.FloatField()
    fecha = models.DateTimeField()
    numero_de_factura = models.FloatField()
    def __str__(self):
        return str (self.numero_de_factura)
class Cliente(models.Model):
    nombre = models.CharField(max_length=64)
    documento = models.CharField(max_length=64)
    direccion = models.CharField(max_length=64)
    correo = models.EmailField(max_length=64)
    tarjeta_de_credito = models.CharField(max_length=64)
    def __str__(self):
        return self.nombre
