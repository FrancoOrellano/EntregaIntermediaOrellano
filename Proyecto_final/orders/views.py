from django.shortcuts import render
from django.http import HttpResponse
from orders.models import Order
from orders.forms import OrderForm

from orders.models import Order
# Create your views here.
def list_orders(request):
    orders = Order.objects.all()
    context = {
        'orders': orders,
    }
    return render(request, 'orders/list_orders.html', context=context)

def create_order(request):
    if request.method == 'GET':
        context = {
            'form': OrderForm()
        }

        return render(request, 'orders/create_order.html', context=context)

    elif request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            Order.objects.create(
                client=form.cleaned_data['client'],
                garment=form.cleaned_data['garment'],
                creation_time=form.data.get,
                payment_method=form.cleaned_data,
            )
            context = {
                'message': 'Orden añadida exitosamente'
            }
            return render(request,'orders/create_order.html', context=context)
        else:
            context = {
                'form_errors': form.errors,
                'form': OrderForm()
            }
            return render(request, 'orders/create_order.html', context=context)