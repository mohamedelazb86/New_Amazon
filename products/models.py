from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from taggit.managers import TaggableManager
from django.utils import timezone
from django.contrib.auth.models import User
FLAG_TYPE=[
    ('New','New'),
    ('Sale','Sale'),
    ('Feature','Feature'),
    ]
class Product(models.Model):

    name=models.CharField(max_length=120,verbose_name=_('name'))
    flag=models.CharField(max_length=50,choices=FLAG_TYPE,verbose_name=_('flag'))
    price=models.FloatField(verbose_name=_('price'))
    image=models.ImageField(upload_to='photo_product',verbose_name=_('image'))
    sku=models.IntegerField(verbose_name=_('sku'))
    subtitle=models.TextField(max_length=5000,verbose_name=_('subtitle'))
    descriptions=models.TextField(max_length=50000,verbose_name=_('descriptions'))
    brand=models.ForeignKey('Brand',related_name='product_brand',on_delete=models.SET_NULL,null=True,blank=True)
    tags = TaggableManager()
    slug=models.SlugField(null=True,blank=True,verbose_name=_('slug'))
    quantity=models.IntegerField(verbose_name=_('quantity'))
    

    def __str__(self):
        return self.name
    
    def save(self,*args,**kwargs):
        self.slug=slugify(self.name)
        super(Product,self).save(*args,**kwargs)


class Brand(models.Model):
    name=models.CharField(max_length=120,verbose_name=_("name"))
    image=models.ImageField(upload_to='photo_brand',verbose_name=_('photo_image'))
    slug=models.SlugField(null=True,blank=True)
    

    def __str__(self):
        return self.name
    
    def save(self,*args,**kwargs):
        self.slug=slugify(self.name)
        super(Brand,self).save(*args,**kwargs)


class Imgae_Product(models.Model):
    product=models.ForeignKey(Product,related_name='image_products',on_delete=models.CASCADE)
    images=models.ImageField(upload_to='images')

    def __str__(self):
        return str(self.product)

class Review(models.Model):
    user=models.ForeignKey(User,related_name='review_user',on_delete=models.SET_NULL,null=True,blank=True)
    product=models.ForeignKey(Product,related_name='review_product',on_delete=models.CASCADE)
    review=models.TextField(max_length=1000)
    publish_date=models.DateTimeField(default=timezone.now)
    rate=models.IntegerField(choices=[(i,i) for i in range(1,6)])

    def __str__(self):
        return f'{self.user}----{self.product}'
    

