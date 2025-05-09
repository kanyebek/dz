from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    def products_count(self):
        return self.products.count()

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    

    def __str__(self):
        return self.title
    
    @property
    def get_rating(self):
        reviews = self.reviews.all()
        if not reviews:
            return 0
        total_stars = sum(review.stars for review in reviews)
        return total_stars / len(reviews)
    
STARS = (
    (i, '* ' * i)for i in range(1,11)
)
class Review(models.Model):
    text = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    stars = models.IntegerField(choices=STARS, default=5)
    def __str__(self):
        return (f'{self.text}, {self.product}')