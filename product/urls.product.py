""" from django.urls import path
from .views import product_detail, product_list

from product.views.product_view import (
    product_list,
    product_create,
    product_delete,
    product_detail,
    product_update,
)

urlpatterns = [
    path('', product_list, name='product_list'),
    path('<int:id>/', product_detail, name='product_detail'),
    path(route='', view=product_list, name='product_list'),
    path(route='create/',view=product_create, name='product_create'),
    path(route='<int:id>/',view=product_detail,name="product_detail"),
    path(route='<int:id>/update/',view=product_update,name="product_update"),
    path(route='<int:id>/delete/',view=product_delete,name="product_delete"),
    path(route='category/', view=category_list, name='category_list'),
]
 """