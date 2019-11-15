from django.urls import path
from . import views


urlpatterns = [
    path('', views.calculator, name='calculator'),
    path('product_list/', views.product_list, name='product_list'),
    path('new_product/', views.new_product, name='new_product'),
    path('edit_product/<int:pk>/', views.edit_product, name='edit_product'),
    path('delete_product/<int:pk>/', views.delete_product, name='delete_product'),
]
