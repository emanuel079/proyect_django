from django.shortcuts import redirect, render
from django.core.paginator import Paginator

from product.models import Category
from product.models import Product
from product.repositories.product import ProductRepository

repo = ProductRepository()


def product_list(request):
    product_list = Product.objects.all()
    paginator = Paginator(product_list, 15)  # Muestra 10 productos por página

    page_number = request.GET.get('page')
    product_list = paginator.get_page(page_number)
    return render(request, 'products/list.html', {'products':  product_list})

def product_detail(request, id):
    producto = repo.get_by_id(id=id)
    return render(request, 'products/detail.html', {"product": producto})

def product_delete(request, id):
    producto = repo.get_by_id(id=id)
    repo.delete(producto=producto)
    return redirect('product_list')

def product_update(request, id):
    product = repo.get_by_id(id=id)
    categorias = Category.objects.all()
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        stock = request.POST.get('stock')
        id_category = request.POST.get('id_category')
        category = Category.objects.get(id=id_category)

        repo.update(
            producto=product,
            nombre=name,
            precio=price,
            descripcion=description,
            stock=stock,
            categoria=category
        )
        return redirect('product_detail', product.id)

    return render(request, 'products/update.html', {'categories': categorias, 'product': product})

def product_create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        stock = request.POST.get('stock')
        id_category = request.POST.get('id_category')
        category = Category.objects.get(id=id_category)

        producto_nuevo = repo.create(
            nombre=name,
            descripcion=description,
            precio=float(price),
            cantidades=stock,
            categoria=category
        )
        return redirect('product_detail', producto_nuevo.id)

    categorias = Category.objects.all()
    return render(request, 'products/create.html', {'categories': categorias})

def product_gte_stock_list(request):
        min_stock = 0
        max_stock = float('inf')
        if request.method == "GET":
            min_stock_str = request.GET.get('min_stock', '0')
            max_stock_str = request.GET.get('max_stock', 'inf')
            print("Valor mínimo de stock recibido en GET:", min_stock_str)
            print("Valor máximo de stock recibido en GET:", max_stock_str)
            
            try:
                min_stock = int(min_stock_str)
                max_stock = int(max_stock_str)
            except ValueError:
                # En caso de que los valores ingresados no sean válidos, se mantienen los valores predeterminados
                pass
            
            # Obtener productos cuyo stock esté dentro del rango especificado
            productos = repo.get_product_stock_range(min_stock, max_stock)
        else:
            productos = repo.get_all()

        return render(  
            request,
            'products/list.html',
            dict(
                products=productos,
                min_stock=min_stock,
                max_stock=max_stock
            ) 
        )


def product_lte_stock_list(request):
        stock_threshold = 0  # Esto puede ser cualquier valor que desees
        productos = repo.get_product_lte_stock(stock_threshold)  
        return render(  
            request,
            'products/list.html',
            dict(
                products=productos  
            ) 
        )





def index_view(request):
    return render(request, 'index/index.html')
