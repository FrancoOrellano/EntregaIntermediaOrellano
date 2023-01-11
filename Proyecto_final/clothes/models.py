from django.db import models

# Create your models here.

class Clothes(models.Model):
    class Meta:
        verbose_name_plural = 'Clothes'
    type = models.CharField(max_length=123, verbose_name= 'Tipo de prenda')
    price = models.FloatField(default=0, verbose_name= 'Precio')
    stock = models.BooleanField(default=False, verbose_name= 'Existencias')

    def __str__(self):
        return self.type

class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=123, unique=True, verbose_name= 'Nombre')