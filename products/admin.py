from django.contrib import admin
from products.models import Category, Product, Review

# Register your models here.
class ReviewInLine(admin.StackedInline):
    model = Review
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    search_fields = ['title', 'description']
    list_filter = ['category', 'price']
    list_display = ['title', 'description', 'price', 'category', 'get_rating']
    list_editable = ['price']
    inlines = [ReviewInLine]


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Review)