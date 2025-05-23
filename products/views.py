from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from products.models import Category, Product, Review
from .serializers import (
    CategorySerializer, CategoryDetailSerializer,
    ProductSerializer, ProductDetailSerializer, ProductReviewSerializer,
    ReviewSerializer, ReviewDetailSerializer, CategoryValidateSerializer, ProductValidateSerializer, ReviewValidateSerializer
)       
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
class CategoriesListAPIVView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = PageNumberPagination
class CategoriesDetailAPIVView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'id'

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = PageNumberPagination
    lookup_field = 'id'

class ProductReviewViewSet(ModelViewSet):   
    queryset = Product.objects.all()
    serializer_class = ProductReviewSerializer
    pagination_class = PageNumberPagination
    lookup_field = 'id'

class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    pagination_class = PageNumberPagination
    lookup_field = 'id'
       
# @api_view(['GET', 'POST'])
# def categories_list_api_view(request):
#     if request.method == 'GET':
#         categories = Category.objects.all()
#         serializer = CategorySerializer(categories, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         validator = CategoryValidateSerializer(data=request.data)
#         if not validator.is_valid():
#             return Response({'error': validator.errors}, status=status.HTTP_400_BAD_REQUEST)
#         name = request.validated_data.get('name')
#         if not name:
#             return Response({'error': 'Name is required'}, status=status.HTTP_400_BAD_REQUEST)
#         category = Category.objects.create(name=name)
#         serializer = CategoryDetailSerializer(category)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


# @api_view(['GET', 'PUT', 'DELETE'])
# def category_detail_api_view(request, id):
#     try:
#         category = Category.objects.get(id=id)
#     except Category.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = CategoryDetailSerializer(category)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         validator = CategoryValidateSerializer(data=request.data)
#         validator.is_valid(raise_exception=True)
#         name = request.validated_data.get('name')
#         if not name:
#             return Response({'error': 'Name is required'}, status=status.HTTP_400_BAD_REQUEST)
#         category.name = name
#         category.save()
#         serializer = CategoryDetailSerializer(category)
#         return Response(serializer.data)

#     elif request.method == 'DELETE':
#         category.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'POST'])
# def products_list_api_view(request):
#     if request.method == 'GET':
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         validator = ProductValidateSerializer(data =request.data)
#         validator.is_valid(raise_exception=True)
#         title = request.validated_data.get('title')
#         description = request.validated_data.get('description')
#         price = request.validated_data.get('price')
#         category_id = request.validated_data.get('category_id')

#         product = Product.objects.create(
#             title=title,
#             description=description,
#             price=price,
#             category_id=category_id
#         )
#         serializer = ProductDetailSerializer(product)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


# @api_view(['GET', 'PUT', 'DELETE'])
# def product_detail_api_view(request, id):
#     try:
#         product = Product.objects.get(id=id)
#     except Product.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = ProductDetailSerializer(product)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         validator = ProductValidateSerializer(data = request.data)
#         validator.is_valid(raise_exception=True)
#         title = request.validated_data.get('title')
#         description = request.validated_data.get('description')
#         price = request.validated_data.get('price')
#         category_id = request.validated_data.get('category_id')

#         product.title = title
#         product.description = description
#         product.price = price
#         product.category_id = category_id
#         product.save()

#         serializer = ProductDetailSerializer(product)
#         return Response(serializer.data)

#     elif request.method == 'DELETE':
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET'])
# def products_with_reviews__api_view(request):
#     products = Product.objects.all()
#     serializer = ProductReviewSerializer(products, many=True)
#     return Response(serializer.data)


# @api_view(['GET', 'POST'])
# def reviews_list_api_view(request):
#     if request.method == 'GET':
#         reviews = Review.objects.all()
#         serializer = ReviewSerializer(reviews, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         validator = ReviewValidateSerializer(data=request.data)
#         validator.is_valid(raise_exception=True)
#         text = request.validated_data.get('text')
#         product_id = request.validated_data.get('product_id')
#         stars = request.validated_data.get('stars')

#         review = Review.objects.create(text=text, product_id=product_id, stars=stars)
#         serializer = ReviewDetailSerializer(review)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


# @api_view(['GET', 'PUT', 'DELETE'])
# def review_detail_api_view(request, id):
#     try:
#         review = Review.objects.get(id=id)
#     except Review.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = ReviewDetailSerializer(review)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         validator = ReviewValidateSerializer(data=request.data)
#         validator.is_valid(raise_exception=True)
#         text = request.validated_data.get('text')
#         product_id = request.validated_data.get('product_id')
#         stars = request.validated_data.get('stars')

#         try:
#             product = Product.objects.get(id=product_id)
#         except Product.DoesNotExist:
#             return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

#         review.text = text
#         review.product_id = product_id
#         review.stars = stars
#         review.save()
#         serializer = ReviewDetailSerializer(review)
#         return Response(serializer.data)

#     elif request.method == 'DELETE':
#         review.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
