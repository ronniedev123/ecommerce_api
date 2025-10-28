from django.contrib import admin
from .models import Product, Category
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'category', 'created_by', 'created_at')
    search_fields = ('name', 'category_name')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_by', 'created_at')


# Register your models here.
