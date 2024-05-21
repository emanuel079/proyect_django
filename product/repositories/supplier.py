from typing import List, Optional
from product.models import Supplier

class SupplierRepository:
       
    def get_all(self) -> List[Supplier]:
        return Supplier.objects.all()
    
    def get_by_id(self, supplier_id: int) -> Optional[Supplier]:
        return Supplier.objects.filter(id=supplier_id).first()

    def filter_by_id(self, id: int) -> Optional[Supplier]:
        return Supplier.objects.filter(id=id).first()

    def create(self, nombre: str, direccion: str, telefono: int = 0):
        return Supplier.objects.create(
            name=nombre,
            address=direccion,
            phone=telefono,
        )

    def update(self, supplier_id: int, name: Optional[str] = None, address: Optional[str] = None, phone: Optional[int] = None):
        supplier = self.get_by_id(supplier_id)
        if supplier:
            if name:
                supplier.name = name
            if address:
                supplier.address = address
            if phone:
                supplier.phone = phone
            supplier.save()
        return supplier
    
    def delete(self, supplier_id: int):
        supplier = self.get_by_id(supplier_id)
        if supplier:
            supplier.delete()
