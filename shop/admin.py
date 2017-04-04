from django.contrib import admin
from .models import Category, Product, City
# Register your models here.
#
# Модель города
class CytiAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}

# Модель категории
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}


# Модель товара
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price',  'tel', 'city', 'category', 'created', 'updated']
    list_filter = ['created', 'updated', 'city', 'category']
    list_editable = ['price',  'tel', 'city', 'category']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(City, CytiAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)

