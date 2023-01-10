from django.db import models

# Create your models here.
class Order(models.Model):
    class Meta:
        verbose_name_plural = 'Orders'
    CHOICES = (
        ('Cash', 'Cash'),
        ('Card', 'Card'),
    )

    client = models.CharField(max_length=123)
    garment = models.CharField(max_length=123)
    creation_time = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(choices=CHOICES, max_length=4)