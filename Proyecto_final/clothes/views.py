from django.shortcuts import render
from django.http import HttpResponse

from clothes.models import Clothes, Category
from clothes.forms import ClothesForm

# Create your views here.

def create_garment(request):
    if request.method == 'GET':
        context = {
            'form': ClothesForm()
        }

        return render(request, 'clothes/create_garment.html', context=context)

    elif request.method == 'POST':
        form = ClothesForm(request.POST)
        if form.is_valid():
            Clothes.objects.create(
                type=form.cleaned_data['type'],
                price=form.cleaned_data['price'],
                stock=form.cleaned_data['stock'],
            )
            context = {
                'message': 'Prenda añadida exitosamente'
            }
            return render(request,'clothes/create_garment.html', context=context)
        else:
            context = {
                'form_errors': form.errors,
                'form': ClothesForm()
            }
            return render(request, 'clothes/create_garment.html', context=context)

def list_clothes(request):
    if 'search' in request.GET:
        search = request.GET['search']
        clothes = Clothes.objects.filter(name__icontains=search)
    else:
        clothes = Clothes.objects.all()
    context= {
        'clothes':clothes,
    }
    return render(request, 'clothes/list_clothes.html', context=context)

def create_category(request, name):
    Category.objects.create(name=name)
    return HttpResponse('Categoría creada')

def list_categories(request):
    all_categories = Category.objects.all()
    context = {
        'categories':all_categories
    }
    return render(request, 'clothes/list_categories.html', context=context)