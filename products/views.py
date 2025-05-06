from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from products.models import Category, Product, Review
from .serializers import CategorySerializer,ProductSerializer, ReviewSerializer,CategoryDetailSerializer, ProductDetailSerializer,ReviewDetailSerializer 

@api_view(http_method_names=['GET'])
def categories_list_api_view(request):
    categories = Category.objects.all()
    data = CategorySerializer(instance = categories, many =True).data
    return Response(data,status=status.HTTP_200_OK)

@api_view(http_method_names=['GET'])
def category_detail_api_view(request, id):
    try:
        category = Category.objects.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data = CategoryDetailSerializer(instance = category, many = False).data
    return Response(data,status=status.HTTP_200_OK)


@api_view(http_method_names=['GET'])
def products_list_api_view(request):
    products = Product.objects.all()
    data = ProductSerializer(instance = products, many = True).data
    return Response(data,status=status.HTTP_200_OK)


@api_view(http_method_names=['GET'])
def product_detail_api_view(request, id):
    try:
        product = Product.objects.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data = ProductDetailSerializer(instance = product, many = False).data
    return Response(data,status=status.HTTP_200_OK)

@api_view(http_method_names=['GET'])
def reviews_list_api_view(request):
    reviews = Review.objects.all()
    data = ReviewSerializer(instance = reviews, many = True).data
    return Response(data,status=status.HTTP_200_OK)


@api_view(http_method_names=['GET'])
def review_detail_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data = ReviewDetailSerializer(instance = review, many = False).data
    return Response(data,status=status.HTTP_200_OK)