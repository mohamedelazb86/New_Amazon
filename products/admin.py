from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Product,Imgae_Product,Brand,Review

class ProductImage(admin.TabularInline):
    model=Imgae_Product

class ProductAdmin(SummernoteModelAdmin):
    list_display=['name','flag','sku']
    list_filter=['brand','flag']
    search_fields=['name','subtitle','descriptions']
    summernote_fields = ('subtitle','descriptions')
    inlines=[ProductImage]
    
admin.site.register(Product,ProductAdmin)
admin.site.register(Brand)
admin.site.register(Review)
#admin.site.register(Imgae_Product)