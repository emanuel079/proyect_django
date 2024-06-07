from typing import List

from django.contrib.auth.models import User

from product.models import ProductReview
from product.repositories.product import ProductRepository

class ProductReviewRepository:

    def get_all(self) -> List[ProductReview]:
        return ProductReview.objects.all()

    def create(
        self,
        product_id: int,
        author: User,
        text: str,
        rating: int
    ) -> ProductReview:
        product_repo = ProductRepository()
        product = product_repo.get_by_id(product_id)
        review = ProductReview.objects.create(
            product=product,
            author=author,
            text=text,
            rating=rating,
        )
        return review
