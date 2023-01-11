from django.urls import path

from orders.views import list_orders, create_order, update_order, OrderDeleteView

urlpatterns = [
    path('list-orders/', list_orders, name='list_orders'),
    path('create-order/', create_order, name='create_order'),
    path('update-order/<int:pk>/', update_order, name='update_order'),
    path('delete-order/<int:pk>/', OrderDeleteView.as_view(), name='delete_order'),
]