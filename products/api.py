from rest_framework import generics
from .serializers import Product_ListSerializers,ProductDetailSerializers,BradDetailSerializers,BrandListSerializers
from .models import Brand,Product



class ProductListApi(generics.ListAPIView):
    queryset=Product.objects.all()
    serializer_class=Product_ListSerializers

class ProductDetaiApi(generics.RetrieveAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductDetailSerializers


class BrandListApi(generics.ListAPIView):
    queryset=Brand.objects.all()
    serializer_class=BrandListSerializers


class BrandDetailApi(generics.RetrieveAPIView):
    queryset=Brand.objects.all()
    serializer_class=BradDetailSerializers

