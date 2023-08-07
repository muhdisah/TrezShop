from django.contrib import admin
from .models import Product, TrendingProduct, RecommendProduct,CartItem


class TrendingProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


class RecommendProductAdmin(admin.ModelAdmin):
    list_display = ('recommend_product',)


# Register your models here.
admin.site.register(TrendingProduct, TrendingProductAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(RecommendProduct, RecommendProductAdmin)
admin.site.register(CartItem)
