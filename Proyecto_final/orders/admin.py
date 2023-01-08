from django.contrib import admin
from orders.models import Order
# Register your models here.

@admin.register(Order)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('client', 'garment', 'creation_time', 'payment_method')
    list_filter = ('client', 'garment')
    search_fields = ('client','garment')