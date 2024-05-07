""" from django.urls import path
from .views import category_list, category_detail

urlpatterns = [
    path(route='category/', view=category_create, name='category_create'),
    path(route='category/<int:id>',view=category_update, name="category_update"),
    path(route='category/<int:id>', view=category_delete, name='category_delete'),
    path(route='category/<int:id>', view=category_list, name='category_list'),
    path(route='<int:id>/',view=category_detail,name="category_detail"),
]
 """