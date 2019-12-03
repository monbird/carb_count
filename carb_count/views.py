from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, JsonResponse
from django.contrib import messages

from .models import Product
from .forms import ProductForm


def calculator(request):
    if request.POST:
        ratio = request.POST.get('ratio', None)
        request.session['ratio'] = ratio
        return JsonResponse({})
    else:
        products = Product.objects.filter(add_to_meal=True)
        return render(request, 'carb_count/calculator.html', {'products': products})


def product_list(request):
    products = Product.objects.all()
    return render(request, 'carb_count/product_list.html', {'products': products})


def product_search(request):
    term = request.GET.get('term', None)
    matching_products = Product.objects.filter(name__icontains=term)
    array = []
    for product in matching_products:
        if product.add_to_meal:
            name = '{} (already on your list)'.format(product.name)
        else:
            name = product.name
        array.append({'label': name, 'value': product.pk, 'selectable': not product.add_to_meal})

    return JsonResponse(array, safe=False)


def create_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()
            p_name = product.name[:15] + '...' if len(product.name) > 15 else product.name
            messages.success(request, 'Product <strong><i>{}</i></strong> has been added successfully to the list.'.format(p_name))
            return redirect('product_list')
        else:
            messages.error(request, '<strong>Warning!</strong> There was a problem with adding your product! Please try again.')
            return render(request, 'carb_count/product_form.html', {'form': form})
    else:
        form = ProductForm()
        return render(request, 'carb_count/product_form.html', {'form': form})


def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            product.save()
            p_name = product.name[:15] + '...' if len(product.name) > 15 else product.name
            messages.success(request, 'Product <strong><i>{}</i></strong> has been updated successfully.'.format(p_name))
            return redirect('product_list')
        else:
            messages.error(request, '<strong>Warning!</strong> There was a problem with updating your product. Please try again.')
            return render(request, 'carb_count/product_form.html', {'form': form, 'edit_mode': True, 'product': product})
    else:
        form = ProductForm(instance=product)
        return render(request, 'carb_count/product_form.html', {'form': form, 'edit_mode': True, 'product': product})


def delete_product(request, pk):
    if request.method == "POST":
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        p_name = product.name[:15] + '...' if len(product.name) > 15 else product.name
        messages.success(request, 'Product <strong><i>{}</i></strong> has been deleted successfully from the list.'.format(p_name))
        return redirect('product_list')
    else:
        raise Http404()


def add_to_meal(request, pk):
    if request.method == "POST":
        product = get_object_or_404(Product, pk=pk)
        product.add_to_meal = True
        product.save()
        if request.is_ajax():
            return JsonResponse({}, status=200)
        else:
            p_name = product.name[:15] + '...' if len(product.name) > 15 else product.name
            messages.success(request, 'Product <strong><i>{}</i></strong> has been added to the meal successfully.'.format(p_name))
            return redirect('product_list')
    else:
        raise Http404()


def remove_from_meal(request, pk):
    if request.method == "POST":
        product = get_object_or_404(Product, pk=pk)
        product.add_to_meal = False
        product.save()
        from_template = request.GET.get('from', None)
        if from_template == "product_list_temp":
            p_name = product.name[:15] + '...' if len(product.name) > 15 else product.name
            messages.success(request, 'Product <strong><i>{}</i></strong> has been removed from the meal successfully.'.format(p_name))
            return redirect('product_list')
        elif from_template == "calc_temp":
            return redirect('calculator')
        else:
            return redirect(request.META['HTTP_REFERER'])
    else:
        raise Http404()
