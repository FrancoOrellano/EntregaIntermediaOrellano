from django.contrib import admin
from clothes.models import Clothes

# Register your models here.

@admin.register(Clothes)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('type', 'price', 'stock')
    list_filter = ('stock',)
    search_fields = ('name',)