from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Product,Brand


class Product_list(ListView):
    model=Product
    template_name='products/product_list.html'

class Product_Detail(DetailView):
    model=Product
    template_name='products/product_detail.html'
    
