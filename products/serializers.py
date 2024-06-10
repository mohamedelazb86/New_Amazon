from rest_framework import serializers
from .models import Product,Brand,Review

class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields='__all__'
class Product_ListSerializers(serializers.ModelSerializer):

    class Meta:
        model=Product
        fields='__all__'

class ProductDetailSerializers(serializers.ModelSerializer):
    brand=serializers.StringRelatedField()
    reviews=ReviewSerializers(source='review_product',many=True)
    class Meta:
        model=Product
        fields='__all__'

class BrandListSerializers(serializers.ModelSerializer):
    class Meta:
        model=Brand
        fields='__all__'

class BradDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model=Brand
        fields='__all__'