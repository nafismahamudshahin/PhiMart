from django.shortcuts import render , get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from product.serializers import ProductSerializer , CategorySerializer
from product.models import Product,Category
# Create your views here.

@api_view()
def view_products(request):
    products = Product.objects.select_related("category").all()
    serializer = ProductSerializer(products, many =True , context={'request': request})
    return Response(serializer.data)

@api_view()
def view_specific_product(request,pk):
    product = get_object_or_404(Product,pk=pk)
    serializer = ProductSerializer(product , context={'request': request})
    return Response(serializer.data)

@api_view()
def view_categorys(request):
    categorys = Category.objects.all()
    serializer = CategorySerializer(categorys, many = True)
    return Response(serializer.data)

@api_view()
def view_specific_category(request,pk):
    category = get_object_or_404(Category , pk = pk)
    serializer = CategorySerializer(category)
    return Response(serializer.data)