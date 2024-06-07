from django.urls import path

from product.views.product_view import (
    product_list,
    product_create,
    product_delete,
    product_detail,
    product_update,
    product_gte_stock_list,
    product_lte_stock_list
)

from product.views.category_view import (
    category_list,
    category_create,
    category_delete,
    category_update,
    category_detail,
)

from product.views.supplier_view import (
    supplier_list,
    supplier_create,
    supplier_delete,
    supplier_update,
    supplier_detail,
)

from product.views.product_review_view import (
    ProductReviewCreateView,
    ProductReviewView,
)

urlpatterns = [
    # URLs de los productos
    path('', product_list, name='product_list'),
    path('create/', product_create, name='product_create'),
    path('<int:id>/', product_detail, name='product_detail'),
    path('<int:id>/update/', product_update, name='product_update'),
    path('<int:id>/delete/', product_delete, name='product_delete'),
    path('stock/gte/', product_gte_stock_list, name='product_gte_stock_list'),
    path('stock/lte/', product_lte_stock_list, name='product_lte_stock_list'),

    # URLs de las categorías
    path('category/', category_list, name='category_list'),
    path('category/create/', category_create, name='category_create'),
    path('category/<int:id>/', category_detail, name='category_detail'),
    path('category/<int:id>/update/', category_update, name='category_update'),
    path('category/<int:id>/delete/', category_delete, name='category_delete'),

    # URLs de los proveedores
    path('supplier/', supplier_list, name='supplier_list'),
    path('supplier/create/', supplier_create, name='supplier_create'),
    path('supplier/<int:supplier_id>/', supplier_detail, name='supplier_detail'),
    path('supplier/<int:supplier_id>/update/', supplier_update, name='supplier_update'),
    path('supplier/<int:supplier_id>/delete/', supplier_delete, name='supplier_delete'),

    # URLs de las reviews de productos
    path('product_reviews/', ProductReviewView.as_view(), name='product_reviews'),
    path('product_reviews/create', ProductReviewCreateView.as_view(), name='product_reviews_create'),
]