from rest_framework import serializers
from product.models import Category , Product
from decimal import Decimal

# class CategorySerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     name = serializers.CharField()
#     description = serializers.CharField()

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name','description','product_cnt']
    product_cnt = serializers.IntegerField()

    # product_cnt = serializers.SerializerMethodField(method_name="products_count")

    # def products_count(self,category):
    #     return Product.objects.filter(category = category).all().count()
        
# class ProductSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     name = serializers.CharField()
#     unit_price = serializers.DecimalField(max_digits=10,decimal_places=2, source ="price")
#     price_with_tax = serializers.SerializerMethodField(method_name="calculate_tax")

#     # category = serializers.PrimaryKeyRelatedField(
#     #     queryset = Category.objects.all()
#     # )
#     # category = serializers.StringRelatedField()
#     # category = CategorySerializer()
#     category_link = serializers.HyperlinkedRelatedField(
#         queryset = Category.objects.all(),
#         view_name = "view-specific-category",
#         source = "category"
#     )

#     def calculate_tax(self,product):
#         return round(product.price * Decimal(1.1),2)

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','name','price','description','stock','category','tax','created_at','updated_at']
    tax = serializers.SerializerMethodField(method_name="calculate_tax")

    category = serializers.HyperlinkedRelatedField(
        queryset = Category.objects.all(),
        view_name = "view-specific-category",
    )

    def calculate_tax(self , product):
        tax = (product.price * Decimal(1.1)) - product.price
        return round(tax,2)
    
    def validate_price(self,price):
        if price<0:
            raise serializers.ValidationError("Nagetive price not possible.")
        