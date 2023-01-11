from django.shortcuts import render
from django.http import HttpResponse

from clothes.models import Clothes, Category
from clothes.forms import ClothesForm, CategoryForm

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
                sex=form.cleaned_data['sex'],
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
        clothes = Clothes.objects.filter(type__icontains=search)
    else:
        clothes = Clothes.objects.all()
    context= {
        'clothes':clothes,
    }
    return render(request, 'clothes/list_clothes.html', context=context)

def create_category(request):
    if request.method == 'GET':
        context = {
            'form': CategoryForm()
        }

        return render(request, 'clothes/categories/create_category.html', context=context)

    elif request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            Category.objects.create(
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
            )
            context = {
                'message': 'Categoría añadida exitosamente'
            }
            return render(request,'clothes/categories/create_category.html', context=context)
        else:
            context = {
                'form_errors': form.errors,
                'form': CategoryForm()
            }
            return render(request, 'clothes/categories/create_category.html', context=context)

def list_categories(request):
    if 'search' in request.GET:
        search = request.GET['search']
        categories = Category.objects.filter(name__icontains=search)
    else:
        categories = Category.objects.all()
    context= {
        'categories':categories,
    }
    return render(request, 'clothes/categories/list_categories.html', context=context)