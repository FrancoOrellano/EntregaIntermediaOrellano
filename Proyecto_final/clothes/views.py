from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DeleteView, UpdateView, ListView, CreateView
from django.db.models import Q

from clothes.models import Clothes, Category
from clothes.forms import ClothesForm, CategoryForm

# Create your views here.
@user_passes_test(lambda u: u.is_superuser)
def create_garment(request):
    if request.method == 'GET':
        context = {
            'form': ClothesForm()
        }

        return render(request, 'clothes/create_garment.html', context=context)

    elif request.method == 'POST':
        form = ClothesForm(request.POST, request.FILES)
        if form.is_valid():
            Clothes.objects.create(
                type=form.cleaned_data['type'],
                price=form.cleaned_data['price'],
                stock=form.cleaned_data['stock'],
                sex=form.cleaned_data['sex'],
                category=form.cleaned_data['category'],
                garment_image=form.cleaned_data['garment_image'],
                size=form.cleaned_data['size'],
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
        clothes = Clothes.objects.filter(Q(type__icontains=search) | Q(category__contains=search,))
    else:
        clothes = Clothes.objects.all()
    context= {
        'clothes':clothes,
    }
    return render(request, 'clothes/list_clothes.html', context=context)

@user_passes_test(lambda u: u.is_superuser)
def update_garment(request, pk):
    garment = Clothes.objects.get(id=pk)

    if request.method == 'GET':
        context = {
            'form': ClothesForm(
                initial={
                    'type':garment.type,
                    'price':garment.price,
                    'stock':garment.stock,
                    'sex':garment.sex,
                    'category':garment.category,
                    'garment_image':garment.garment_image,
                    'size':garment.size,
                }
            )
        }

        return render(request, 'clothes/update_garment.html', context=context)

    elif request.method == 'POST':
        form = ClothesForm(request.POST, request.FILES)
        if form.is_valid():
            garment.type = form.cleaned_data['type']
            garment.price = form.cleaned_data['price']
            garment.stock = form.cleaned_data['stock']
            garment.sex = form.cleaned_data['sex']
            garment.category = form.cleaned_data['category']
            garment.garment_image = form.cleaned_data['garment_image']
            garment.size = form.cleaned_data['size']
            garment.save()
            
            context = {
                'message': 'Prenda actualizada'
            }
        else:
            context = {
                'form_errors': form.errors,
                'form': ClothesForm()
            }
        return render(request, 'clothes/update_garment.html', context=context)

@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
class GarmentDeleteView(DeleteView):
    model = Clothes
    template_name = 'clothes/delete_garment.html'
    success_url = '/clothes/list-clothes/'

@user_passes_test(lambda u: u.is_superuser)
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

@user_passes_test(lambda u: u.is_superuser)
def update_category(request, pk):
    provider = Category.objects.get(id=pk)

    if request.method == 'GET':
        context = {
            'form': CategoryForm(
                initial={
                    'name':provider.name,
                    'description':provider.description,
                }
            )
        }

        return render(request, 'clothes/categories/update_category.html', context=context)

    elif request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            provider.name = form.cleaned_data['name']
            provider.description = form.cleaned_data['description']
            provider.save()
            
            context = {
                'message': 'Categoría actualizada'
            }
        else:
            context = {
                'form_errors': form.errors,
                'form': CategoryForm()
            }
        return render(request, 'clothes/categories/update_category.html', context=context)

@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'clothes/categories/delete_category.html'
    success_url = '/clothes/list-categories/'