from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    class Meta:
        verbose_name_plural = 'Perfiles de usuarios'
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', verbose_name='Usuario')
    phone = models.CharField(max_length=25, null=True, blank=True, verbose_name='Numero telefonico')
    birth_date = models.DateField(null=True, blank=True, verbose_name='Fecha de nacimiento')
    profile_picture = models.ImageField(upload_to='profile_images', null=True, blank=True)
