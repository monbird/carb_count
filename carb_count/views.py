from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.contrib import messages
from .models import Product
from .forms import ProductForm


def calculator(request):
    return render(request, 'carb_count/calculator.html')


def product_list(request):
    products = Product.objects.all()
    return render(request, 'carb_count/product_list.html', {'products': products})


def new_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have added your product successfully.')
            return redirect('product_list')
        else:
            messages.error(request, 'There was a problem with adding your product.')
    else:
        form = ProductForm()
        return render(request, 'carb_count/new_product.html', {'form': form})


def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            product.save()
            messages.success(request, 'You have updated your product successfully.')
            return redirect('product_list')
        else:
            messages.error(request, 'There was a problem with updating your product.')
    else:
        form = ProductForm(instance=product)
    return render(request, 'carb_count/edit_product.html', {'form': form})


def delete_product(request, pk):
    if request.method == "POST":
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        messages.success(request, 'You have deleted your product successfully.')
        return redirect('product_list')
    else:
        raise Http404()
