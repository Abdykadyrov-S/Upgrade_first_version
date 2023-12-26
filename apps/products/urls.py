from django.urls import path 

from .views import *

urlpatterns = [
    path('products/', products, name='products'),
    path('category/', category, name='category'),
    path('sub_category/', sub_category, name='sub_category'),
    path('product_list/', product_list, name='product_list'),
    path('category/<str:slug>/', category_detail, name="category_detail"),
    path('product_detail/<int:id>/', product_detail, name='product_detail'),
    path('search/', search, name='search'),
]