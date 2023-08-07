from django.contrib import admin
from .models import New


# Register your models here.
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'post')


admin.site.register(New, NewsAdmin)
