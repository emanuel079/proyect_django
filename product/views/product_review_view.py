from django.shortcuts import redirect, render
from django.views import View

from product.repositories.product import ProductRepository
from product.repositories.product_reviews import ProductReviewRepository


class ProductReviewView(View):
    def get(self, request, *args, **kwargs):
        repo = ProductReviewRepository()
        reviews = repo.get_all()
        return render(
            request,
            'product_reviews/list.html',
            dict(
                reviews=reviews
            )
        )
    

class ProductReviewCreateView(View):
    def get(self, request, *args, **kwargs):
        repo = ProductRepository()
        products = repo.get_all()
        return render(
            request,
            'product_reviews/create.html',
            dict(
                products=products
            )
        )
    
    def post(self, request):
        repo = ProductReviewRepository()

        product_id = request.POST.get('id_producto')
        review = request.POST.get('opinion')
        value = request.POST.get('valoracion')
        user = request.user

        repo.create(
            product_id=product_id,
            author=user,
            text=review,
            rating=value,
        )
        return redirect('product_reviews')
