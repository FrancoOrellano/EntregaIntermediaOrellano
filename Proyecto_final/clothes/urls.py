from django.urls import path

from clothes.views import create_garment, list_clothes, list_categories, create_category


urlpatterns = [
    path('create-garment/', create_garment),
    path('list-clothes/', list_clothes),

    path('create-category/<str:name>/', create_category),
    path('list-categories/', list_categories),
]