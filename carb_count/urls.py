from django.urls import path
from . import views


urlpatterns = [
    # path('', views.calculate, name='calculate'),
    path('product_list/', views.product_list, name='product_list'),
    # path('add_product/', views.add_product, name='add_product'),
]
