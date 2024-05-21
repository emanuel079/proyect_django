from django.shortcuts import redirect, render


from product.repositories.category import CategoryRepository
from product.repositories.product import ProductRepository



category_repo = CategoryRepository()

def category_list(request):
    category_repository = CategoryRepository()
    categorias = category_repository.get_all()
    return render(
        request,
        'categories/list.html',
        dict(
            categories=categorias
        )
    )

def category_detail(request, id:int):
    category_repository = CategoryRepository()
    product_repository = ProductRepository()
    categoria = category_repository.get_by_id(id)
    productos = product_repository.filter_by_category(categoria)
    return render(
        request,
        'categories/detail.html',
        dict(   
            category=categoria,
            products=productos,
        )
    )


def category_delete(request, id):
    categoria = category_repo.get_by_id(id)  
    category_repo.delete(categoria)
    return redirect('category_list')
            



def category_update(request, id):
    category = category_repo.get_by_id(id)
    if request.method == "POST":
        name = request.POST.get('name')
        category_repo.update(category, name)
        return redirect('category_detail', category.id)
    
    return render(
        request,
        'categories/update.html',
        dict(
            category=category,
        )
    )


def category_create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        # Aquí podrías añadir validaciones o manejo de errores según sea necesario
        category_repo.create(name)
        return redirect('category_list')
    
    return render(
        request, 
        'categories/create.html'
        )






