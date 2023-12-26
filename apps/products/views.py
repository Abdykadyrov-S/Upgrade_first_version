from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.db.models import Q

from apps.settings.models import Settings, About
from .models import Product, Category

import json

# Create your views here.
# def category(request):
#     title_page = "Категории"
#     categories = Category.objects.filter(parent=None).order_by("?")
#     settings = Settings.objects.latest('id')
#     footer_categories = Category.objects.all().order_by('?')
#     return render(request, 'service/shop-category.html', locals())

def category(request):
    title_page = "Услуги"
    categories = Category.objects.filter(parent=None).order_by("?")
    settings = Settings.objects.latest('id')
    footer_categories = Category.objects.filter(parent=None).order_by("?")
    return render(request, 'service/category.html', locals())

def sub_category(request):
    title_page = "Под Категории услуг"
    parent_slug = request.GET.get('parent_slug')
    if parent_slug:
        parent_category = get_object_or_404(Category, slug=parent_slug)
        subcategories = parent_category.subcategories.all()
    else:
        subcategories = Category.objects.filter(parent=None)
    settings = Settings.objects.latest('id')
    footer_categories = Category.objects.filter(parent=None).order_by("?")
    return render(request, 'service/sub-category.html', locals())

def category_detail(request, slug):
    title_page = "Услуги и товары"
    settings = Settings.objects.latest('id')
    category = Category.objects.get(slug=slug)
    products = Product.objects.filter(category=category)
    footer_categories = Category.objects.filter(parent=None).order_by("?")
    return render(request, 'service/category-details.html', locals())



def products(request):
    title_page = "Услуги и товары"
    categories = Category.objects.all()
    settings = Settings.objects.latest('id')
    all_products = Product.objects.all().order_by('?')
    about = About.objects.latest('id')
    footer_categories = Category.objects.filter(parent=None).order_by("?")
    return render(request, 'service/all_products.html', locals())


def product_detail(request, id):
    title_page = "Услуги"
    settings = Settings.objects.latest('id')
    product = Product.objects.get(id=id)
    about = About.objects.latest('id')
    footer_categories = Category.objects.filter(parent=None).order_by("?")
    
    return render(request, 'service/product-details.html', locals())


def product_list(request):
    title_page = "Сортировка товаров"
    settings = Settings.objects.latest('id')
    all_products = Product.objects.all()
    footer_categories = Category.objects.filter(parent=None).order_by("?")

    print(request.GET.get('min_price'))
    min_price_param = request.GET.get('min_price')
    if min_price_param is not None:
        try:
            print(request.GET.get('min_price'))
            user_prices = request.GET.get('min_price').replace(" ", "").split("-")
            print(user_prices)
            min_price = int(user_prices[0])
            max_price = int(user_prices[1])
            all_products = Product.objects.filter(price__range=(min_price, max_price))
            print(all_products)
        except (ValueError, IndexError):
            pass

    popular = request.GET.get('popular', False)
    product_day = request.GET.get('product_day', False)
    new = request.GET.get('new', False)
    featured = request.GET.get('featured', False)

    if popular:
        all_products = all_products.filter(popular=True)
    if product_day:
        all_products = all_products.filter(product_day=True)
    if new:
        all_products = all_products.filter(new=True)
    if featured:
        all_products = all_products.filter(featured=True)

    return render(request, 'service/all_products.html', locals())


def search(request):
    query = request.GET.get('q', '')
    if query:
        results = Product.objects.filter(Q(title__icontains=query) | Q(description__icontains=query) | Q(image__icontains=query)).order_by('-created')[:5]
        print(results.values('id', 'title', 'description', 'image'))
        data = list(results.values('id', 'title', 'description', 'image')) 
        return JsonResponse(data, safe=False)
    return JsonResponse([])
