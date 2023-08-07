from django.db import models
from django.conf import settings


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    item_description = models.TextField()
    stock = models.IntegerField()
    image_url = models.ImageField(upload_to='static/product-image')

    def __str__(self):
        return self.name


class TrendingProduct(models.Model):
    name = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_name')
    CATEGORY_CHOICES = (
        ('laptop', 'Laptop'),
        ('desktop', 'Desktop'),
        ('printer', 'Printer'),
        ('accessories', 'Accessories'),
    )
    category = models.CharField(max_length=15, choices=CATEGORY_CHOICES)



class RecommendProduct(models.Model):
    recommend_product = models.ForeignKey(Product, on_delete=models.CASCADE)


class CartItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    # Add any additional fields you need, like quantity or timestamp

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"

