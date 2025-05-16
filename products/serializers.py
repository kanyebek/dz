from rest_framework import serializers
from products.models import Category, Product, Review

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'products_count']

class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'category']
    def get_category(self, product):
        return product.category.name

class ProductReviewSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    rating = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'category', 'reviews', 'rating']
        depth = 1
    def get_category(self, product):
        return product.category.name
    def get_rating(self, product):
        return product.get_rating

class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id','text', 'product']

class ReviewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class CategoryValidateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    def validate_name(self, value):
        if Category.objects.filter(name=value).exists():
            raise serializers.ValidationError("Category with this name already exists.")
        return value
    
class ProductValidateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length = 100)
    description = serializers.CharField(required = False)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    category_id = serializers.IntegerField(min_value=1)

    def validate_title(self, value):
        if Product.objects.filter(title=value).exists():
            raise serializers.ValidationError("Product with this title already exists.")
        return value
    
    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be positive.")
        return value

    def validate_category_id(self, value):
        if not Category.objects.filter(id=value).exists():
            raise serializers.ValidationError("Category not found.")
        return value
    
class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField(max_length = 1000)
    product_id = serializers.IntegerField(min_value =1)
    stars = serializers.IntegerField(min_value = 1, max_value=5)
    def validate_product_id(self, value):
        if not Product.objects.filter(id=value).exists():
            raise serializers.ValidationError("Product not found.")
        return value
