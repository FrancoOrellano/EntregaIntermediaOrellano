from django.db import models

# Create your models here.

class Clothes(models.Model):
    type = models.CharField(max_length=123)
    price = models.FloatField
    stock = models.BooleanField(default=False)

    def __str__(self):
        return self.type

class Category(models.Model):
    name = models.CharField(max_length=123, unique=True)