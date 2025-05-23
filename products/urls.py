from django.urls import path
from products.views import CategoriesListAPIVView, CategoriesDetailAPIVView,ProductViewSet, ReviewViewSet, ProductReviewViewSet
# from products.views import (
#     categories_list_api_view, category_detail_api_view,
#     products_list_api_view, product_detail_api_view,
#     reviews_list_api_view, review_detail_api_view,
#     products_with_reviews__api_view
# )

urlpatterns = [
    path('categories/', CategoriesListAPIVView.as_view()),
    path('categories/<int:id>/', CategoriesDetailAPIVView.as_view()),
    path('', ProductViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('<int:id>/', ProductViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('reviews/', ProductReviewViewSet.as_view({'get': 'list', 'post': 'create'})),
]