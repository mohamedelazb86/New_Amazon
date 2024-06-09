from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView
from .models import Product,Brand,Review,Imgae_Product
from django.db.models.aggregates import Count


class Product_list(ListView):
    model=Product
    template_name='products/product_list.html'
    paginate_by=20

class Product_Detail(DetailView):
    model=Product
    template_name='products/product_detail.html'

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context["reviews"] = Review.objects.filter(product=self.get_object()).order_by('-id')[:3]
        context["images"] = Imgae_Product.objects.filter(product=self.get_object())
        context["products"] =Product.objects.filter(brand=self.get_object().brand)
        return context


class Brand_list(ListView):
    model=Brand
    template_name='products/brand_list.html'
    paginate_by=20
    
    queryset=Brand.objects.annotate(product_count=Count('product_brand'))
    

class Brand_detail(DetailView):
    model=Brand
    template_name='products/brand_detail.html'
    
    
def add_review(request,slug):
    product=Product.objects.get(slug=slug)
   

    review=request.POST['review']
    rate=request.POST['rating']
    Review.objects.create(
        product=product,
        user=request.user,
        review=review,
        rate=rate,

    )
    return redirect(f'/products/{slug}')
        

