from django.db import models

# Create your models here.

class Clothes(models.Model):
    CHOICES = (
    ('man', 'Hombre'),
    ('woman', 'Mujer'),
    ('unisex', 'Unisex'),
)
    CATEGORIES = (
        ('Buzos', 'Buzos'),
        ('Remeras', 'Remeras'),
        ('Gorras', 'Gorras'),
    )
    class Meta:
        verbose_name_plural = 'Prendas'
    type = models.CharField(max_length=123, verbose_name= 'Prenda')
    price = models.FloatField(default=0, verbose_name= 'Precio')
    stock = models.BooleanField(default=False, verbose_name= 'Existencias')
    sex = models.CharField(choices = CHOICES, max_length= 6, default= 'unisex', verbose_name = 'Sexo')
    category = models.CharField(choices = CATEGORIES, max_length= 7, default= 'shirts', verbose_name= 'Categoría')
    garment_image = models.ImageField(upload_to='products_img', null=True, blank=True, verbose_name= 'Foto de la prenda')
    size = models.CharField(max_length=123, verbose_name= 'Talles')

    def __str__(self):
        return self.type

class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categorias'
    name = models.CharField(max_length=123, unique=True, verbose_name= 'Nombre')
    description = models.CharField(max_length=123, default= 'Sin descripción', verbose_name= 'Descripción')