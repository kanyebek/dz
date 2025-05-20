from django.urls import path
from products.views import (
    categories_list_api_view, category_detail_api_view,
    products_list_api_view, product_detail_api_view,
    reviews_list_api_view, review_detail_api_view,
    products_with_reviews__api_view
)

urlpatterns = [
    path('categories/', categories_list_api_view),
    path('categories/<int:id>/', category_detail_api_view),
    path('products/', products_list_api_view),
    path('products/<int:id>/', product_detail_api_view),
    path('products/reviews/', products_with_reviews__api_view),
    path('reviews/', reviews_list_api_view),
    path('reviews/<int:id>/', review_detail_api_view),  
]