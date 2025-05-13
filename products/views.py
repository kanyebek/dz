from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from products.models import Category, Product, Review
from .serializers import (
    CategorySerializer, CategoryDetailSerializer,
    ProductSerializer, ProductDetailSerializer, ProductReviewSerializer,
    ReviewSerializer, ReviewDetailSerializer
)

@api_view(['GET', 'POST'])
def categories_list_api_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        name = request.data.get('name')
        if not name:
            return Response({'error': 'Name is required'}, status=status.HTTP_400_BAD_REQUEST)
        category = Category.objects.create(name=name)
        serializer = CategoryDetailSerializer(category)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def category_detail_api_view(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CategoryDetailSerializer(category)
        return Response(serializer.data)

    elif request.method == 'PUT':
        name = request.data.get('name')
        if not name:
            return Response({'error': 'Name is required'}, status=status.HTTP_400_BAD_REQUEST)
        category.name = name
        category.save()
        serializer = CategoryDetailSerializer(category)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def products_list_api_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        title = request.data.get('title')
        description = request.data.get('description')
        price = request.data.get('price')
        category_id = request.data.get('category')

        if not all([title, description, price, category_id]):
            return Response({'error': 'All fields are required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)

        product = Product.objects.create(
            title=title,
            description=description,
            price=price,
            category=category
        )
        serializer = ProductDetailSerializer(product)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def product_detail_api_view(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductDetailSerializer(product)
        return Response(serializer.data)

    elif request.method == 'PUT':
        title = request.data.get('title')
        description = request.data.get('description')
        price = request.data.get('price')
        category_id = request.data.get('category')

        if not all([title, description, price, category_id]):
            return Response({'error': 'All fields are required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)

        product.title = title
        product.description = description
        product.price = price
        product.category = category
        product.save()

        serializer = ProductDetailSerializer(product)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def products_with_reviews__api_view(request):
    products = Product.objects.all()
    serializer = ProductReviewSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def reviews_list_api_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        text = request.data.get('text')
        product_id = request.data.get('product')

        if not all([text, product_id]):
            return Response({'error': 'Text and product are required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

        review = Review.objects.create(text=text, product=product)
        serializer = ReviewDetailSerializer(review)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ReviewDetailSerializer(review)
        return Response(serializer.data)

    elif request.method == 'PUT':
        text = request.data.get('text')
        product_id = request.data.get('product')

        if not all([text, product_id]):
            return Response({'error': 'Text and product are required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

        review.text = text
        review.product = product
        review.save()
        serializer = ReviewDetailSerializer(review)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
