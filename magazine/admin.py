from django.contrib import admin

from . models import Category, Product



class CategoryAdmin(admin.ModelAdmin):
    list_fields = ['name', ]

class ProductAdmin(admin.ModelAdmin):
    list_fields = ['category', 'name', 'price']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
