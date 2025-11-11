from django.shortcuts import render , get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from product.serializers import ProductSerializer
from product.models import Product
# Create your views here.

@api_view()
def view_products(request):
    products = Product.objects.all()
    all_products =[]
    for product in products:
        products_dist = {}
        products_dist['id'] = product.id
        products_dist['name'] = product.name
        products_dist['price'] = product.price
        all_products.append(products_dist)
    return Response(all_products)

@api_view()
def view_specific_product(request,id):
    product = get_object_or_404(Product,pk=id)
    serializer = ProductSerializer(product)
    return Response(serializer.data)

@api_view()
def view_categorys(request):
    return Response("this is categorys")