from django.db import models

# Create your models here.

class Clothes(models.Model):
    class Meta:
        verbose_name_plural = 'Clothes'
    type = models.CharField(max_length=123)
    price = models.FloatField(default=0)
    stock = models.BooleanField(default=False)

    def __str__(self):
        return self.type

class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=123, unique=True)