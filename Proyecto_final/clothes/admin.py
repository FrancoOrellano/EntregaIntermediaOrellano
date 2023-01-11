from django.contrib import admin
from clothes.models import Clothes, Category

# Register your models here.

@admin.register(Clothes)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('type', 'price', 'stock', 'sex')
    list_filter = ('stock',)
    search_fields = ('name',)

@admin.register(Category)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)