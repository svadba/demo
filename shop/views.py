from django.shortcuts import render, get_object_or_404
from .models import Category, Product, City
from cart.forms import CartAddProductForm
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.



#
# class VProducts(ListView):
#     template_name = 'shop/index.html'
#     context_object_name = 'vproducts'
#     model = Product
#     def get_queryset(self):
#         qs = Product.objects.all()
#         return qs
#
class ProductCityList(ListView):
    template_name = 'shop/category/city.html'
    context_object_name = 'products'
    model = Product
    def get_queryset(self):
        city_filter = self.request.GET.get('city', '')
        cat_filter = self.request.GET.get('category', '').split(',')
        if not isinstance(cat_filter, (list, tuple)):
            cat_filter = list(cat_filter)
        products = Product.objects.all()
        if city_filter:
            products = products.filter(city=city_filter)
        if cat_filter:
            products = products.filter(category__slug__in=cat_filter)
        return products

# # Страница с товарами
# def ProductList(request, category_slug=None):
#     category = None
#     categories = Category.objects.all()
#     products = Product.objects.all()
#     if category_slug:
#         category = get_object_or_404(Category, slug=category_slug)
#         products = products.filter(category=category)
#     return render(request, 'shop/category/product/list.html', {
#         'category': category,
#         'categories': categories,
#         'products': products
#     })

# Страница товара
def ProductDetail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug)
    cart_product_form = CartAddProductForm
    return render(request, 'shop/category/product/detail.html', {'product': product, 'cart_product_form': cart_product_form})

# class ProductCatCityList(ProductCityList):
#     template_name = 'shop/category/product/list.html'
#     context_object_name = 'category'



# Должны получать товары по городу и категории
# class CityListView(ListView):
#     template_name = 'shop/category/city.html'
#     context_object_name = 'products'
#     # model = Product
#
#     def get_queryset(self):
#         city = City.objects.get(city__slug=self.kwargs['slug'])
#         category = Category.objects.get(category_slug=self.kwargs['slug'])
#         products = Product.objects.filter(city=city, category=category)
#         # products = Product.objects.filter(city__slug=self.kwargs['slug'])
#         # Отбираем первые 10 статей
#         paginator = Paginator(products, 1)
#         page = self.request.GET.get('page')
#         try:
#             products = paginator.page(page)
#         except PageNotAnInteger:
# Если страница не является целым числом, поставьте первую страницу.
#             products = paginator.page(1)
#         except EmptyPage:
# Если страница находится за пределами допустимого диапазона (9999) доставьте последнюю страницу результатов
#             products = paginator.page(paginator.num_pages)
#         return products



class A(ListView):
    template_name = 'shop/base.html'
    context_object_name = 'products'
    model = Product
    def get_queryset(self):
        city = City.objects.get(slug=self.kwargs['slug'])
        products = Product.objects.filter(city=city)
        return products

    def productList(self, category_slug=None):
        category = None
        categories = Category.objects.all()
        products = Product.objects.all()
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            products = products.filter(category=category)
        return render('shop/category/product/list.html', {
            'category': category,
            'categories': categories,
            'products': products
        })

