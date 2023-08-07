from django.shortcuts import render
from products.models import Product, RecommendProduct
from products.models import TrendingProduct
from news.models import New


# Create your views here.
def index(request):
    products = Product.objects.all()
    trending = TrendingProduct.objects.all()
    tech_news = New.objects.all()
    recommend_item = RecommendProduct.objects.all()
    context = {'products': products, 'trending': trending, 'news': tech_news,'recommend_item': recommend_item}
    return render(request, 'index.html', context)
