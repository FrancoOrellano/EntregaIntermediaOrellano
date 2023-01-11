from django.urls import path

from clothes.views import create_garment, list_clothes, list_categories, create_category, update_garment, GarmentDeleteView, update_category, CategoryDeleteView


urlpatterns = [
    path('create-garment/', create_garment, name='create_garment'),
    path('list-clothes/', list_clothes, name='list_clothes'),
    path('update-garment/<int:pk>/', update_garment, name='update_garment'),
    path('delete-garment/<int:pk>/', GarmentDeleteView.as_view(), name='delete_garment'),

    path('create-category/', create_category, name='create_category'),
    path('list-categories/', list_categories, name='list_categories'),
    path('update-category/<int:pk>/', update_category, name='update_category'),
    path('delete-category/<int:pk>/', CategoryDeleteView.as_view(), name='delete_category'),
]