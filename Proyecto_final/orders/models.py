from django.db import models

# Create your models here.
class Order(models.Model):
    class Meta:
        verbose_name_plural = 'Orders'
    CHOICES = (
        ('Cash', 'Efectivo'),
        ('Card', 'Tarjeta'),
    )

    client = models.CharField(max_length=123, verbose_name= 'Cliente')
    garment = models.CharField(max_length=123, verbose_name= 'Prenda')
    creation_time = models.DateTimeField(auto_now_add=True, verbose_name= 'Fecha de creación')
    payment_method = models.CharField(choices=CHOICES, max_length=4, verbose_name= 'Metodo de pago')