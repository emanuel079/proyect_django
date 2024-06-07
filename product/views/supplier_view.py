from django.shortcuts import render, get_object_or_404, redirect
from product.repositories.supplier import SupplierRepository
from product.models import Supplier
from django.contrib.auth.decorators import login_required






supplier_repo = SupplierRepository()

def supplier_list(request):
    suppliers = supplier_repo.get_all()
    return render(request, 'supplier/list.html', {'suppliers': suppliers})

def supplier_detail(request, supplier_id):
    supplier = get_object_or_404(Supplier, id=supplier_id)
    return render(request, 'supplier/detail.html', {'supplier': supplier})

def supplier_delete(request, supplier_id):
    supplier_repo.delete(supplier_id)
    return redirect('supplier_list')

@login_required(login_url='login')
def supplier_update(request, supplier_id):
    supplier = supplier_repo.get_by_id(supplier_id)
    if request.method == "POST":
        name = request.POST.get('name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        
        # Actualiza los atributos del proveedor
        supplier.name = name
        supplier.address = address
        supplier.phone = phone
        supplier.save()

        return redirect('supplier_list')

    return render(request, 'supplier/update.html', {'supplier': supplier})

@login_required(login_url='login')
def supplier_create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')        

        supplier_repo.create(
            nombre=name,
            direccion=address,
            telefono=phone,
        )
        return redirect('supplier_list')
    return render(request, 'supplier/create.html')