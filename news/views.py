from django.shortcuts import render
from .models import New


# Create your views here.
def news(request):
    tech_news = New.objects.all()
    return render(request, 'news.html', {'news': tech_news})

