from django.urls import path
from . import views


urlpatterns = [
    path('', views.calculator, name='calculator'),
    path('product/list/', views.product_list, name='product_list'),
    path('product/create/', views.create_product, name='create_product'),
    path('product/<int:pk>/edit/', views.edit_product, name='edit_product'),
    path('product/<int:pk>/delete/', views.delete_product, name='delete_product'),
    path('product/<int:pk>/add_to_meal/', views.add_to_meal, name='add_to_meal'),
    path('product/<int:pk>/remove_from_meal/', views.remove_from_meal, name='remove_from_meal'),
]
