from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from orders.models import Order
from orders.forms import OrderForm

from orders.models import Order
# Create your views here.
@user_passes_test(lambda u: u.is_superuser)
def list_orders(request):
    if 'search' in request.GET:
        search = request.GET['search']
        orders = Order.objects.filter(garment__icontains=search)
    else:
        orders = Order.objects.all()
    context= {
        'orders':orders,
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
                payment_method=form.cleaned_data['payment_method'],
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

@user_passes_test(lambda u: u.is_superuser)
def update_order(request, pk):
    provider = Order.objects.get(id=pk)

    if request.method == 'GET':
        context = {
            'form': OrderForm(
                initial={
                    'client':provider.client,
                    'garment':provider.garment,
                    'payment_method':provider.payment_method,
                }
            )
        }

        return render(request, 'orders/update_order.html', context=context)

    elif request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            provider.client = form.cleaned_data['client']
            provider.garment = form.cleaned_data['garment']
            provider.payment_method = form.cleaned_data['payment_method']
            provider.save()
            
            context = {
                'message': 'Orden actualizada'
            }
        else:
            context = {
                'form_errors': form.errors,
                'form': OrderForm()
            }
        return render(request, 'orders/update_order.html', context=context)

@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'orders/delete_order.html'
    success_url = '/orders/list-orders/'
