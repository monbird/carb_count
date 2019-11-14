from django.shortcuts import render


def product_list(request):
    return render(request, 'carb_count/product_list.html', {})
