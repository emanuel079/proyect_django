from django.urls import path


from product.views.product_view import (
    product_list,
    product_create,
    product_delete,
    product_detail,
    product_update,
)
from product.views.category_view import (
    category_list,
    category_create,
    category_delete,
    category_update,
    category_detail,
)

urlpatterns = [
    #   URLs de los productos
    path(route='', view=product_list, name='product_list'),
    path(route='create/',view=product_create, name='product_create'),
    path(route='<int:id>/',view=product_detail,name="product_detail"),
    path(route='<int:id>/update/',view=product_update,name="product_update"),
    path(route='<int:id>/delete/',view=product_delete,name="product_delete"),
    path(route='category/', view=category_list, name='category_list'),
    

     #   URLs de las categorias
    path(route='category/create/', view=category_create, name='category_create'),
    path(route='category/<int:id>/update/',view=category_update, name="category_update"),
    path(route='category/<int:id>/delete/', view=category_delete, name='category_delete'),
    path(route='category/<int:id>/', view=category_list, name='category_list'),
    path(route='<int:id>/detail/',view=category_detail,name="category_detail"),
    
]

""" 
urlpatterns = [
    path('', product_list, name='index'),
    path('products/', include('urls.product')),  # Agrupar URLs de productos bajo /products/
    path('categories/', include('urls.category')),  # Agrupar URLs de categorías bajo /categories/
] """
