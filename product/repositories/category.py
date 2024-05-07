from typing import List, Optional

from product.models import Category

class CategoryRepository:

    def get_all(self)-> List[Category]:
        return Category.objects.all()    
    
    
    def filter_by_id(self, id: int) -> Optional[Category]:
        return Category.objects.filter(id=id).first()
    
    def get_by_id(self, id: int) -> Optional[Category]:
        try:
            category = Category.objects.get(id=id)
        except:
            category = None
        return category
    
    def create(
        self,
        nombre: str,
    ):
        return Category.objects.create(
            name=nombre,
        )
    
    def delete(self, category: Category):
        return category.delete()
    
    def update(
        self, 
        categoria: Category,
        nombre: str,
    ) -> Category:

        categoria.name = nombre
        
        categoria.save()